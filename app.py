from flask import Flask, request, jsonify, render_template

from security import is_safe_domain

from database import (
    create_tables,
    get_scan_history,
    add_domain,
    get_domains,
    delete_domain
)


app = Flask(__name__)


# ==========================================
# HOME / DASHBOARD
# ==========================================

@app.route("/")
def dashboard():

    return render_template("index.html")


# ==========================================
# SCAN API
# ==========================================

@app.route("/scan", methods=["POST"])
def scan():

    data = request.get_json()

    # Check that JSON data was provided
    if not data:

        return jsonify({
            "error": "Request body is required"
        }), 400


    # Check that domain was provided
    if "domain" not in data:

        return jsonify({
            "error": "Domain is required"
        }), 400


    domain = data["domain"].strip()


    # Check that domain is not empty
    if not domain:

        return jsonify({
            "error": "Domain cannot be empty"
        }), 400


    # SSRF protection
    if not is_safe_domain(domain):

        return jsonify({
            "error": "Domain is not allowed"
        }), 400


    # --------------------------------------
    # TEMPORARY SCAN RESPONSE
    # --------------------------------------
    #
    # We will connect the real SiteGuard
    # scanner here later.
    #

    return jsonify({

        "message": "Scan request accepted",

        "domain": domain,

        "score": 0

    })


# ==========================================
# SCAN HISTORY
# ==========================================

@app.route("/history", methods=["GET"])
def history():

    scans = get_scan_history()

    results = []


    for scan in scans:

        results.append({

            "domain": scan["domain"],

            "score": scan["score"],

            "scanned_at": scan["scanned_at"]

        })


    return jsonify(results)


# ==========================================
# ADD DOMAIN
# ==========================================

@app.route("/domains", methods=["POST"])
def create_domain():

    data = request.get_json()


    if not data:

        return jsonify({
            "error": "Request body is required"
        }), 400


    if "domain" not in data:

        return jsonify({
            "error": "Domain is required"
        }), 400


    domain = data["domain"].strip()


    if not domain:

        return jsonify({
            "error": "Domain cannot be empty"
        }), 400


    # SSRF protection
    if not is_safe_domain(domain):

        return jsonify({
            "error": "Domain is not allowed"
        }), 400


    # Try to add the domain
    if add_domain(domain):

        return jsonify({

            "message": "Domain added",

            "domain": domain

        }), 201


    return jsonify({

        "error": "Domain already exists"

    }), 409


# ==========================================
# VIEW DOMAINS
# ==========================================

@app.route("/domains", methods=["GET"])
def domains():

    domain_list = get_domains()

    results = []


    for domain in domain_list:

        results.append({

            "id": domain["id"],

            "domain": domain["domain"],

            "added_at": domain["added_at"]

        })


    return jsonify(results)


# ==========================================
# DELETE DOMAIN
# ==========================================

@app.route(
    "/domains/<int:domain_id>",
    methods=["DELETE"]
)
def remove_domain(domain_id):

    delete_domain(domain_id)


    return jsonify({

        "message": "Domain deleted"

    })


# ==========================================
# ERROR HANDLER
# ==========================================

@app.errorhandler(Exception)
def handle_error(error):

    return jsonify({

        "error": "Unable to process request",

        "reason": str(error)

    }), 500


# ==========================================
# START SITEGUARD
# ==========================================

if __name__ == "__main__":

    # Make sure database tables exist
    create_tables()


    app.run(

        host="127.0.0.1",

        port=5000,

        debug=False

    )
