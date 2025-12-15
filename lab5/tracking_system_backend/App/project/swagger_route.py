from flask import Blueprint, jsonify, request, current_app
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = "/swagger"
API_URL = "/swagger.json"

swagger_bp = Blueprint("swagger_bp", __name__)
swagger_ui_bp = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={"app_name": "Lab5 API"})

METHODS_ALLOWED = {"GET", "POST", "PUT", "PATCH", "DELETE"}
EXCLUDE_ENDPOINTS = {"static"}
EXCLUDE_RULE_PREFIXES = {SWAGGER_URL}

def _skip(rule):
    if rule.endpoint in EXCLUDE_ENDPOINTS: return True
    p = str(rule.rule)
    return p.startswith(SWAGGER_URL) or not (rule.methods and METHODS_ALLOWED.intersection(rule.methods))

def _autogen():
    host = request.host
    scheme = request.scheme if request.scheme in ("http", "https") else "http"
    paths = {}
    for rule in current_app.url_map.iter_rules():
        if _skip(rule): continue
        path = str(rule.rule).replace("<", "{").replace(">", "}")
        methods = sorted(m.lower() for m in METHODS_ALLOWED.intersection(rule.methods or set()))
        if not methods: continue
        paths.setdefault(path, {})
        for m in methods:
            paths[path][m] = {
                "summary": f"{m.upper()} {path}",
                "parameters": [],
                "responses": {
                    "200": {"description": "OK"},
                    "201": {"description": "Created"},
                    "204": {"description": "No Content"},
                    "400": {"description": "Bad Request"},
                    "404": {"description": "Not Found"},
                    "500": {"description": "Server Error"},
                },
            }
    return {
        "swagger": "2.0",
        "info": {"title": "Lab5 API (auto)", "version": "1.0.0"},
        "host": host,
        "basePath": "/",
        "schemes": [scheme],
        "paths": paths,
    }

@swagger_bp.route("/swagger.json")
def swagger_json():
    return jsonify(_autogen())
