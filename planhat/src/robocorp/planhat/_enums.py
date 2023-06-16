from enum import Enum


class PlanhatObjectTypes(Enum):
    COMPANIES = "companies"
    COMPANY = "companies"
    ENDUSERS = "endusers"
    ENDUSER = "endusers"
    LICENSES = "licenses"
    LICENSE = "licenses"
    ASSETS = "assets"
    ASSET = "assets"
    CAMPAIGNS = "campaigns"
    CAMPAIGN = "campaigns"
    CHURNS = "churns"
    CHURN = "churns"
    CONVERSIONS = "conversions"
    CONVERSION = "conversions"
    INVOICES = "invoices"
    INVOICE = "invoices"
    ISSUES = "issues"
    ISSUE = "issues"
    NOTES = "notes"
    NOTE = "notes"
    OPPORTUNITIES = "opportunities"
    OPPORTUNITY = "opportunities"
    NPS = "nps"
    OBJECTIVES = "objectives"
    OBJECTIVE = "objectives"
    PROJECTS = "projects"
    PROJECT = "projects"
    SALES = "sales"
    SALE = "sales"
    TASKS = "tasks"
    TASK = "tasks"
    WORKSPACES = "workspaces"
    WORKSPACE = "workspaces"
    USERS = "users"
    USER = "users"


class PlanhatIdTypes(Enum):
    SOURCE = "srcid-"
    SRC = "srcid-"
    SRCID = "srcid-"
    SOURCE_ID = "srcid-"
    SOURCEID = "srcid-"
    EXTERNAL = "ext-"
    EXT = "ext-"
    EXTID = "ext-"
    EXTERNAL_ID = "ext-"
    EXTERNALID = "ext-"
