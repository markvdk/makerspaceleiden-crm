from django.urls import path

from . import views

urlpatterns = [
    path("me", views.member_overview, name="my_page"),
    path("acl/personal_page", views.member_overview, name="personal_page"),
    path("acl/member/<int:member_id>", views.member_overview, name="overview"),
    path(
        "acl/member/delete/<int:member_id>",
        views.member_delete_confirm,
        name="userdelete",
    ),
    path(
        "acl/member/delete_confirm/<int:member_id>",
        views.member_delete,
        name="userdelete_confirm",
    ),
    path("acl/member/", views.members, name="overview"),
    path("acl/tag/edit/<int:tag_id>", views.tag_edit, name="tag_edit"),
    path("acl/tag/delete/<int:tag_id>", views.tag_delete, name="tag_delete"),
    path(
        "acl/machine/<int:machine_id>", views.machine_overview, name="machine_overview"
    ),
    path("acl/machine/", views.machine_overview, name="machine_overview"),
    path("acl/machines", views.machine_list, name="machine_list"),
    # For the trusteeds - to ease admin.
    path("acl/missing_forms/", views.missing_forms, name="missing_forms"),
    path("acl/missing_doors/", views.missing_doors, name="missing_doors"),
    path("acl/filed_forms/", views.filed_forms, name="filed_forms"),
    # Convenience page to debug the API
    path("acl/", views.api_index, name="acl-index"),
    # API calls
    #
    # calls to give an ok/nok for a machine or node given a tag. Requires
    # a bearer token or superuser credentials along with a valid tag.
    #
    path("acl/api/v1/getok/<str:machine>", views.api_getok, name="acl-v1-getok"),
    path(
        "acl/api/v1/getok4node/<str:node>",
        views.api_getok_by_node,
        name="acl-v1-getok4-node",
    ),
    # Provide metadata on a tag, requires a valid tag and a bearer token.
    #
    # path("acl/api/v1/gettaginfo", views.api_gettaginfo, name="acl-v1-gettaginfo"),
    # Provide metadata on a machine - propably no longer used. Requires
    # a bearer token.
    #
    path("acl/<int:machine_id>", views.api_details, name="details"),
    path(
        "acl/api/v1/getchangecounter",
        views.api_getchangecounter,
        name="acl-v1-getchangecounter",
    ),
    path(
        "acl/api/v1/getchangecounterJSON",
        views.api_getchangecounterJSON,
        name="acl-v1-getchangecounterJSON",
    ),
    # calls to provide all tags for a given node/machine. Requires a valid
    # terminal cert.
    #
    # Plaintext versions disabled; binary/encrypted version appears to work
    # will. Will likely be removed.
    #
    #    path(
    #        "acl/api/v1/gettags4node/<str:node>",
    #        views.api_gettags4node,
    #        name="acl-v1-gettags",
    #    ),
    #    path(
    #        "acl/api/v1/gettags4machineJSON/<str:machine>",
    #        views.api_gettags4machineJSON,
    #        name="acl-v1-gettags-json",
    #    ),
    #    path(
    #        "acl/api/v1/gettags4machineCSV/<str:machine>",
    #        views.api_gettags4machineCSV,
    #        name="acl-v1-gettags-csv",
    #    ),
    path(
        "acl/api/v1/gettags4machineBIN/<str:machine>",
        views.api_gettags4machineBIN,
        name="acl-v1-gettags-bin",
    ),
]
