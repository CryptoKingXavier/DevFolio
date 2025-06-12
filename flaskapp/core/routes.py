from http import HTTPMethod, HTTPStatus
from flask import Blueprint, render_template, url_for


core: Blueprint = Blueprint("core", __name__, template_folder="templates", static_folder="static", static_url_path="/")


# TODO: Index Route
@core.route("/", methods=[HTTPMethod.GET.value])
def index(): return render_template("core/index.html", body_style="index-page"), HTTPStatus.OK.value

# TODO: Starter Page Route
@core.route("/starter-page/", methods=[HTTPMethod.GET.value])
def starter_page(): return render_template("core/starter-page.html", body_style="starter-page-page"), HTTPStatus.OK.value

# TODO: Service Details Route
@core.route("/service-details/", methods=[HTTPMethod.GET.value])
def service_details(): return render_template("core/service-details.html", body_style="service-details-page"), HTTPStatus.OK.value

# TODO: Portfolio Details Route
@core.route("/portfolio-details/", methods=[HTTPMethod.GET.value])
def portfolio_details(): return render_template("core/portfolio-details.html", body_style="portfolio-details-page"), HTTPStatus.OK.value
