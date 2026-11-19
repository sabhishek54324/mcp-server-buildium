"""Generated Buildium tools: one per Buildium API operation not covered by the hand-written tools.

DO NOT EDIT BY HAND. Regenerate with scripts/gen_all_tools.py from specs/buildium-openapi-2026-11-19.json.
Write tools are named create_*, update_* or delete_* by HTTP method, so agents can deny them by prefix.
"""

from typing import Annotated, Any

from fastmcp import FastMCP
from pydantic import Field

from ..buildium_client import BuildiumClient

GENERATED_TOOL_COUNT = 387


def register_generated_tools(mcp: FastMCP, client: BuildiumClient) -> None:
    """Register every generated Buildium tool."""

    @mcp.tool(name="get_application_transactions", description="[Application Transactions] Retrieve all application transactions. Retrieves all the transactions for a specific application. Required permission(s): Rentals > Lease transactions - `View`")
    async def get_application_transactions(
        application_id: Annotated[int, Field(description="applicationId")],
        ids: Annotated[list[int] | None, Field(description="Filters results to specific transactions by their unique identifiers. If not specified, all application transactions will be returned.")] = None,
        transactiondatefrom: Annotated[str | None, Field(description="Filters results to any application transaction whose start date is greater than or equal to the specified value. The date must be formatted as YYYY-MM-DD")] = None,
        transactiondateto: Annotated[str | None, Field(description="Filters results to any application transaction whose end date is less than or equal to the specified value. The date must be formatted as YYYY-MM-DD")] = None,
        transactiontypes: Annotated[list[str] | None, Field(description="Filters results to any application transaction whose application transaction type matches the specified types. If no type is specified, application transactions with any type will be returned.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/applications/{applicationId}/transactions", path_params={"applicationId": application_id}, query={"ids": ids, "transactiondatefrom": transactiondatefrom, "transactiondateto": transactiondateto, "transactiontypes": transactiontypes, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_committees", description="[Committees] Retrieve all association committees. Retrieves all association committees. Currently only supports sorting by one field at a time. Required permission(s): Associations > Associations and units - `View` Associations > Ownership accounts - `View` Associations > Association owners and tenants - `View`")
    async def get_committees(
        association_id: Annotated[int, Field(description="associationId")],
        ids: Annotated[list[int] | None, Field(description="Filters results to only records that belong to the specified set of committee identifiers.")] = None,
        committeename: Annotated[str | None, Field(description="Filters results to only records whose name *contains* the specified value.")] = None,
        committeedescription: Annotated[str | None, Field(description="Filters results to only records whose description *contains* the specified value.")] = None,
        committeestatuses: Annotated[list[str] | None, Field(description="Filters results by the status of the committee. If no statuses are specified, committees with any status will be returned.")] = None,
        createddatetimefrom: Annotated[str | None, Field(description="Filters results to only records that were created after this date. Must be formatted as `YYYY-MM-DDTHH:MM:SSZ`.")] = None,
        createddatetimeto: Annotated[str | None, Field(description="Filters results to only records that were created before this date. Must be formatted as `YYYY-MM-DDTHH:MM:SSZ`.")] = None,
        lastupdateddatetimefrom: Annotated[str | None, Field(description="Filters results to only records that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
        lastupdateddatetimeto: Annotated[str | None, Field(description="Filters results to only records that were updated on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
        startdatefrom: Annotated[str | None, Field(description="Filters results to only records that were started on or after the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        startdateto: Annotated[str | None, Field(description="Filters results to only records that were started on or before the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/{associationId}/committees", path_params={"associationId": association_id}, query={"ids": ids, "committeename": committeename, "committeedescription": committeedescription, "committeestatuses": committeestatuses, "createddatetimefrom": createddatetimefrom, "createddatetimeto": createddatetimeto, "lastupdateddatetimefrom": lastupdateddatetimefrom, "lastupdateddatetimeto": lastupdateddatetimeto, "startdatefrom": startdatefrom, "startdateto": startdateto, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_ownership_account_ledger", description="[Ownership Account Transactions] Retrieve all transactions. Retrieves all ledger transactions for a specific ownership account. Required permission(s): Associations > Ownership account transactions - `View`")
    async def get_ownership_account_ledger(
        ownership_account_id: Annotated[int, Field(description="The ownership account identifier.")],
        transactiondatefrom: Annotated[str | None, Field(description="Filters results to any lease transaction whose start date is greater than or equal to the specified value.")] = None,
        transactiondateto: Annotated[str | None, Field(description="Filters results to any lease transaction whose end date is less than or equal to the specified value.")] = None,
        transactiontypes: Annotated[list[str] | None, Field(description="Filters results to any lease transaction whose lease transaction type matches the specified status. If no type is specified, lease transactions with any type will be returned.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/ownershipaccounts/{ownershipAccountId}/transactions", path_params={"ownershipAccountId": ownership_account_id}, query={"transactiondatefrom": transactiondatefrom, "transactiondateto": transactiondateto, "transactiontypes": transactiontypes, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_architectural_requests", description="[Architectural Requests] Retrieve all architectural requests. Retrieves all architectural requests. Required permission(s): Associations > Associations and units - `View` Associations > Ownership accounts - `View` Associations > Association owners and tenants - `View` Associations > Architectural requests - `View`")
    async def get_architectural_requests(
        associationids: Annotated[list[int] | None, Field(description="Filters results to only records that belong to the specified set of association identifiers.")] = None,
        ownershipaccountids: Annotated[list[int] | None, Field(description="Filters results to only records that belong to the specified set of ownership account identifiers.")] = None,
        ids: Annotated[list[int] | None, Field(description="Filters results to only records that belong to the specified set of architectural request identifiers.")] = None,
        statuses: Annotated[list[str] | None, Field(description="Filters results to only records whose status is equal to the specified value.")] = None,
        decisions: Annotated[list[str] | None, Field(description="Filters results to only records whose decision is equal to the specified value.")] = None,
        createddatetimefrom: Annotated[str | None, Field(description="Filters results to only records that were created after this date. Must be formatted as `YYYY-MM-DDTHH:MM:SSZ`.")] = None,
        createddatetimeto: Annotated[str | None, Field(description="Filters results to only records that were created before this date. Must be formatted as `YYYY-MM-DDTHH:MM:SSZ`.")] = None,
        lastupdatedfrom: Annotated[str | None, Field(description="Filters results to only records that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
        lastupdatedto: Annotated[str | None, Field(description="Filters results to only records that were updated on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
        submitteddatetimefrom: Annotated[str | None, Field(description="Filters results to only records that were submitted on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
        submitteddatetimeto: Annotated[str | None, Field(description="Filters results to only records that were submitted on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/ownershipaccounts/architecturalrequests", path_params={}, query={"associationids": associationids, "ownershipaccountids": ownershipaccountids, "ids": ids, "statuses": statuses, "decisions": decisions, "createddatetimefrom": createddatetimefrom, "createddatetimeto": createddatetimeto, "lastupdatedfrom": lastupdatedfrom, "lastupdatedto": lastupdatedto, "submitteddatetimefrom": submitteddatetimefrom, "submitteddatetimeto": submitteddatetimeto, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_architectural_request_async", description="[Architectural Requests] Create an architectural request. Creates an architectural request Required permission(s): Associations > Associations and units - `View` `Edit` Associations > Ownership accounts - `View` `Edit` Associations > Architectural requests - `View` `Edit` Associations > Association owners and tenants - `View` `Edit`")
    async def create_architectural_request_async(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/associations/ownershipaccounts/architecturalrequests", path_params={}, query={}, body=body)

    @mcp.tool(name="get_inventory_assets", description="[Inventory and Assets] Retrieve all inventory assets. Retrieves a list of inventory assets. Required permission(s): Maintenance > Inventory and Assets - `View`")
    async def get_inventory_assets(
        entitytype: Annotated[str | None, Field(description="Filters results to inventory assets associated with the specified entity type.")] = None,
        entityid: Annotated[int | None, Field(description="Filters results to inventory assets associated with the specified entity identifier.")] = None,
        unitids: Annotated[list[int] | None, Field(description="Filters results to inventory assets associated with the specified unit identifiers.")] = None,
        inventorystorageids: Annotated[list[int] | None, Field(description="Filters results to inventory assets stored in the specified inventory storage identifiers.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/inventoryassets", path_params={}, query={"entitytype": entitytype, "entityid": entityid, "unitids": unitids, "inventorystorageids": inventorystorageids, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_lease_ledgers", description="[Lease Transactions] Retrieve all lease transactions. Retrieves all the transactions for a specific lease. Required permission(s): Rentals > Lease transactions - `View`")
    async def get_lease_ledgers(
        lease_id: Annotated[int, Field(description="leaseId")],
        transactiondatefrom: Annotated[str | None, Field(description="Filters results to any lease transaction whose start date is greater than or equal to the specified value.")] = None,
        transactiondateto: Annotated[str | None, Field(description="Filters results to any lease transaction whose end date is less than or equal to the specified value.")] = None,
        transactiontypes: Annotated[list[str] | None, Field(description="Filters results to any lease transaction whose lease transaction type matches the specified status. If no type is specified, lease transactions with any type will be returned.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/{leaseId}/transactions", path_params={"leaseId": lease_id}, query={"transactiondatefrom": transactiondatefrom, "transactiondateto": transactiondateto, "transactiontypes": transactiontypes, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_all_users", description="[Administration] Retrieve all users. Retrieves a list of users. Required permission(s): Administration > Users - `View`")
    async def get_all_users(
        roleids: Annotated[list[int] | None, Field(description="Describes the role of the user.")] = None,
        usertypes: Annotated[list[str] | None, Field(description="Describes the user type of the user.")] = None,
        status: Annotated[str | None, Field(description="Filters results by the status of the user. If no status is specified both `active` and `inactive` staff members will be returned.")] = None,
        name: Annotated[str | None, Field(description="Filters results to only records whose name *contains* the specified value.")] = None,
        email: Annotated[str | None, Field(description="Filters results to only records whose email *contains* the specified value.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/users", path_params={}, query={"roleids": roleids, "usertypes": usertypes, "status": status, "name": name, "email": email, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_lease_ledger_transaction_by_id", description="[Application Transactions] Retrieve an application transaction. Retrieves a specific application transaction. Required permission(s): Rentals > Lease Transactions - `View`")
    async def get_lease_ledger_transaction_by_id(
        application_id: Annotated[int, Field(description="applicationId")],
        transaction_id: Annotated[int, Field(description="transactionId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/applications/{applicationId}/transactions/{transactionId}", path_params={"applicationId": application_id, "transactionId": transaction_id}, query={}, body=None)

    @mcp.tool(name="get_committee", description="[Committees] Retrieve an association committee. Retrieves an association committee. Required permission(s): Associations > Associations and units - `View` Associations > Ownership accounts - `View` Associations > Association owners and tenants - `View`")
    async def get_committee(
        association_id: Annotated[int, Field(description="associationId")],
        committee_id: Annotated[int, Field(description="committeeId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/{associationId}/committees/{committeeId}", path_params={"associationId": association_id, "committeeId": committee_id}, query={}, body=None)

    @mcp.tool(name="get_ownership_account_transaction_by_id", description="[Ownership Account Transactions] Retrieve a transaction. Retrieves a specific ownership account ledger transaction. Required permission(s): Associations > Ownership account transactions - `View`")
    async def get_ownership_account_transaction_by_id(
        ownership_account_id: Annotated[int, Field(description="The ownership account identifier.")],
        transaction_id: Annotated[int, Field(description="The transaction identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/ownershipaccounts/{ownershipAccountId}/transactions/{transactionId}", path_params={"ownershipAccountId": ownership_account_id, "transactionId": transaction_id}, query={}, body=None)

    @mcp.tool(name="get_architectural_request_by_id", description="[Architectural Requests] Retrieve an architectural request. Retrieves a specific architectural request. Required permission(s): Associations > Associations and units - `View` Associations > Ownership accounts - `View` Associations > Association owners and tenants - `View` Associations > Architectural requests - `View`")
    async def get_architectural_request_by_id(
        architectural_request_id: Annotated[int, Field(description="architecturalRequestId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/ownershipaccounts/architecturalrequests/{architecturalRequestId}", path_params={"architecturalRequestId": architectural_request_id}, query={}, body=None)

    @mcp.tool(name="get_lease_ledger_transaction_by_id_lease_transactions", description="[Lease Transactions] Retrieve a lease transaction. Retrieves a specific lease transaction. Required permission(s): Rentals > Lease Transactions - `View`")
    async def get_lease_ledger_transaction_by_id_lease_transactions(
        lease_id: Annotated[int, Field(description="leaseId")],
        transaction_id: Annotated[int, Field(description="transactionId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/{leaseId}/transactions/{transactionId}", path_params={"leaseId": lease_id, "transactionId": transaction_id}, query={}, body=None)

    @mcp.tool(name="get_listing_for_unit_async", description="[Listings] Retrieve a listing. Retrieves a specific listing. Required permission(s): Rentals > Listings - `View` Rentals > Rental properties and units - `View`")
    async def get_listing_for_unit_async(
        unit_id: Annotated[int, Field(description="The rental unit identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/rentals/units/{unitId}/listing", path_params={"unitId": unit_id}, query={}, body=None)

    @mcp.tool(name="update_upsert_listings_async", description="[Listings] Create/Update a listing. This endpoint can be used to both *create* and *update* a listing. If no listing exists for the unit one will be created, otherwise the existing listing will be updated. A unit can only ever have one active listing. Upon creation the listing will post immediately to your Buildium public website, and will post to the selected syndicated sites within 24-48 hours. Updates to the listing will appear immediately in your Buildium public website and propagated to syndicated sites within 24-48 hours. Note, the listing will automatically pull in the information, features, and media that exists for the property and unit details. Rentals > Listings - `View` `Edit` Rentals > Rental properties and units - `View` `Edit`")
    async def update_upsert_listings_async(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        unit_id: Annotated[int, Field(description="unitId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/rentals/units/{unitId}/listing", path_params={"unitId": unit_id}, query={}, body=body)

    @mcp.tool(name="delete_delist_unit", description="[Listings] Delete a listing. Deleting a listing will immediately remove it from your Buildium public website. The listing will also be removed from any syndicated sites within 24-48 hours. Listings manually created on craigslist using the Buildium guided tool will not be removed. The listing must be removed using craigslist's tools provided in your craigslist account. Required permission(s): Rentals > Listings - `View` `Edit` `Delete`")
    async def delete_delist_unit(
        unit_id: Annotated[int, Field(description="The rental property unit identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("DELETE", "/v1/rentals/units/{unitId}/listing", path_params={"unitId": unit_id}, query={}, body=None)

    @mcp.tool(name="get_user_by_id", description="[Administration] Retrieve a user. Retrieve a specific user. Required permission(s): Administration > Users - `View`")
    async def get_user_by_id(
        user_id: Annotated[int, Field(description="The user identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/users/{userId}", path_params={"userId": user_id}, query={}, body=None)

    @mcp.tool(name="get_application_outstanding_balances", description="[Application Transactions] Retrieve all outstanding balances. Retrieves a list of applications that have outstanding balances. Applications with a zero or credit balance will not be returned in the results. Required permission(s): Rentals > Outstanding Balances - `View`")
    async def get_application_outstanding_balances(
        applicationstatuses: Annotated[list[str] | None, Field(description="Filters results to applications in specific statuses. If not specified, all application outstanding balances will be returned.")] = None,
        applicationids: Annotated[list[int] | None, Field(description="Filters results to specific applications by their unique identifiers. If not specified, all application outstanding balances will be returned.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/applications/outstandingbalances", path_params={}, query={"applicationstatuses": applicationstatuses, "applicationids": applicationids, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_architectural_request_files_history_paged_async", description="[Architectural Requests] Retrieve all files for an architectural request. Retrieves all files for an architectural request. Required permission(s): Associations > Associations and units - `View` Associations > Ownership accounts - `View` Associations > Association owners and tenants - `View` Associations > Architectural requests - `View`")
    async def get_architectural_request_files_history_paged_async(
        architectural_request_id: Annotated[int, Field(description="architecturalRequestId")],
        ids: Annotated[list[int] | None, Field(description="The IDs of the architectural request files to filter by.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/ownershipaccounts/architecturalrequests/{architecturalRequestId}/files", path_params={"architecturalRequestId": architectural_request_id}, query={"ids": ids, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_ownership_account_outstanding_balances", description="[Ownership Account Transactions] Retrieve all outstanding balances. Retrieves a list of ownership account outstanding balances. Required permission(s): Associations > Outstanding Balances - `View`")
    async def get_ownership_account_outstanding_balances(
        associationid: Annotated[int | None, Field(description="Association unique identifier")] = None,
        ownershipaccountstatuses: Annotated[list[str] | None, Field(description="List of ownership account statuses")] = None,
        ownershipaccountids: Annotated[list[int] | None, Field(description="List of ownership account ids")] = None,
        pastdueemail: Annotated[str | None, Field(description="Status of notification of outstanding balances")] = None,
        balanceduration: Annotated[str | None, Field(description="Duration of outstanding balances")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/ownershipaccounts/outstandingbalances", path_params={}, query={"associationid": associationid, "ownershipaccountstatuses": ownershipaccountstatuses, "ownershipaccountids": ownershipaccountids, "pastdueemail": pastdueemail, "balanceduration": balanceduration, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_all_association_units", description="[Association Units] Retrieve all units. Retrieves a list of association units. Required permission(s): Associations > Associations and units - `View`")
    async def get_all_association_units(
        associationids: Annotated[list[int] | None, Field(description="Filters results to only include Associations with matching IDs")] = None,
        lastupdatedfrom: Annotated[str | None, Field(description="Filters results to any association units that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
        lastupdatedto: Annotated[str | None, Field(description="Filters results to any association units that were updated on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/units", path_params={}, query={"associationids": associationids, "lastupdatedfrom": lastupdatedfrom, "lastupdatedto": lastupdatedto, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_inventory_asset", description="[Inventory and Assets] Create an inventory asset. Creates an inventory asset. Required permission(s): Maintenance > Inventory and Assets - `View` `Edit`")
    async def create_inventory_asset(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/inventoryasset", path_params={}, query={}, body=body)

    @mcp.tool(name="get_lease_outstanding_balances", description="[Lease Transactions] Retrieve all outstanding balances. Retrieves a list of leases that have outstanding balances. Leases with a zero or credit balance will not be returned in the results. Required permission(s): Rentals > Outstanding Balances - `View`")
    async def get_lease_outstanding_balances(
        entitytype: Annotated[str | None, Field(description="entitytype")] = None,
        entityid: Annotated[int | None, Field(description="entityid")] = None,
        leasestatuses: Annotated[list[str] | None, Field(description="leasestatuses")] = None,
        leaseids: Annotated[list[int] | None, Field(description="leaseids")] = None,
        pastdueemail: Annotated[str | None, Field(description="pastdueemail")] = None,
        balanceduration: Annotated[str | None, Field(description="balanceduration")] = None,
        evictionstatus: Annotated[str | None, Field(description="evictionstatus")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/outstandingbalances", path_params={}, query={"entitytype": entitytype, "entityid": entityid, "leasestatuses": leasestatuses, "leaseids": leaseids, "pastdueemail": pastdueemail, "balanceduration": balanceduration, "evictionstatus": evictionstatus, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_all_listing_contacts", description="[Listings] Retrieve all listing contacts. Retrieves all listing contacts. Required permission(s): Rentals > Listings - `View`")
    async def get_all_listing_contacts(
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/rentals/units/listingcontacts", path_params={}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_listing_contact", description="[Listings] Create a listing contact. Create a listing contact. Note, at least one contact field (phone number, email or website) is required for the listing contact. Required permission(s): Rentals > Listings - `View` `Edit`")
    async def create_listing_contact(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/rentals/units/listingcontacts", path_params={}, query={}, body=body)

    @mcp.tool(name="get_all_user_roles", description="[Administration] Retrieve all user roles. Retrieves a list of user roles. Required permission(s): Administration > User Roles - `View`")
    async def get_all_user_roles(
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/userroles", path_params={}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_application_charges", description="[Application Transactions] Retrieve all charges. Retrieves all the charges for a specific application. Required permission(s): Rentals > Lease transactions - `View`")
    async def get_application_charges(
        application_id: Annotated[int, Field(description="applicationId")],
        chargeids: Annotated[list[int] | None, Field(description="Filters results by charge ids")] = None,
        transactiondatefrom: Annotated[str | None, Field(description="Filters results to any application transaction whose start date is greater than or equal to the specified value.")] = None,
        transactiondateto: Annotated[str | None, Field(description="Filters results to any application transaction whose end date is less than or equal to the specified value.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/applications/{applicationId}/charges", path_params={"applicationId": application_id}, query={"chargeids": chargeids, "transactiondatefrom": transactiondatefrom, "transactiondateto": transactiondateto, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_application_ledger_charge", description="[Application Transactions] Create a charge. Creates a charge on a specific application ledger. Required permission(s): Rentals > Lease transactions - `View` `Edit`")
    async def create_application_ledger_charge(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        application_id: Annotated[int, Field(description="applicationId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/applications/{applicationId}/charges", path_params={"applicationId": application_id}, query={}, body=body)

    @mcp.tool(name="get_all_ownership_account_charges", description="[Ownership Account Transactions] Retrieve all charges. Retrieves all ledger charges for a specific ownership account. Required permission(s): Associations > Ownership account transactions - `View`")
    async def get_all_ownership_account_charges(
        ownership_account_id: Annotated[int, Field(description="ownershipAccountId")],
        transactiondatefrom: Annotated[str | None, Field(description="Filters results to any lease transaction whose start date is greater than or equal to the specified value.")] = None,
        transactiondateto: Annotated[str | None, Field(description="Filters results to any lease transaction whose end date is less than or equal to the specified value.")] = None,
        billids: Annotated[list[int] | None, Field(description="Filters results to any charge that has been associated to the indicated bill ids.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/ownershipaccounts/{ownershipAccountId}/charges", path_params={"ownershipAccountId": ownership_account_id}, query={"transactiondatefrom": transactiondatefrom, "transactiondateto": transactiondateto, "billids": billids, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_charge", description="[Ownership Account Transactions] Create a charge. Creates a ledger charge. Required permission(s): Associations > Ownership account transactions - `View` `Edit` Accounting > Bills - `View` `Edit` In order to associate the charge to a bill using the BillId property, you must have this permission.")
    async def create_charge(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        ownership_account_id: Annotated[int, Field(description="The ownership account identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/associations/ownershipaccounts/{ownershipAccountId}/charges", path_params={"ownershipAccountId": ownership_account_id}, query={}, body=body)

    @mcp.tool(name="get_association_unit_by_id", description="[Association Units] Retrieve a unit. Retrieve a specific association unit. Required permission(s): Associations > Associations and units - `View`")
    async def get_association_unit_by_id(
        unit_id: Annotated[int, Field(description="The association unit identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/units/{unitId}", path_params={"unitId": unit_id}, query={}, body=None)

    @mcp.tool(name="get_inventory_asset_by_id", description="[Inventory and Assets] Retrieve an inventory asset. Retrieves a specific inventory asset. Required permission(s): Maintenance > Inventory and Assets - `View`")
    async def get_inventory_asset_by_id(
        inventory_asset_id: Annotated[int, Field(description="inventoryAssetId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/inventoryasset/{inventoryAssetId}", path_params={"inventoryAssetId": inventory_asset_id}, query={}, body=None)

    @mcp.tool(name="update_inventory_asset", description="[Inventory and Assets] Update an inventory asset. Updates an inventory asset. Required permission(s): Maintenance > Inventory and Assets - `View` `Edit`")
    async def update_inventory_asset(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        inventory_asset_id: Annotated[int, Field(description="inventoryAssetId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/inventoryasset/{inventoryAssetId}", path_params={"inventoryAssetId": inventory_asset_id}, query={}, body=body)

    @mcp.tool(name="delete_inventory_asset", description="[Inventory and Assets] Delete an inventory asset. Deletes an inventory asset and its associated service history. Any tasks linked to the asset will be unlinked. Required permission(s): Maintenance > Inventory and Assets - `View` `Edit` `Delete`")
    async def delete_inventory_asset(
        inventory_asset_id: Annotated[int, Field(description="inventoryAssetId")],
    ) -> dict[str, Any]:
        return await client.raw_request("DELETE", "/v1/inventoryasset/{inventoryAssetId}", path_params={"inventoryAssetId": inventory_asset_id}, query={}, body=None)

    @mcp.tool(name="get_all_charges", description="[Lease Transactions] Retrieve all charges. Retrieves all the charges for a specific lease. Required permissions(s): Rentals > Lease transactions - `View`")
    async def get_all_charges(
        lease_id: Annotated[int, Field(description="leaseId")],
        transactiondatefrom: Annotated[str | None, Field(description="Filters results to any lease transaction whose start date is greater than or equal to the specified value.")] = None,
        transactiondateto: Annotated[str | None, Field(description="Filters results to any lease transaction whose end date is less than or equal to the specified value.")] = None,
        billids: Annotated[list[int] | None, Field(description="Filters results to any charge that has been associated to the indicated bill ids.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/{leaseId}/charges", path_params={"leaseId": lease_id}, query={"transactiondatefrom": transactiondatefrom, "transactiondateto": transactiondateto, "billids": billids, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_charge_lease_transactions", description="[Lease Transactions] Create a charge. Creates a charge transaction on a specific lease ledger. Required permission(s): Rentals > Lease transactions - `View` `Edit` Accounting > Bills - `View` `Edit` In order to associate the charge to a bill using the BillId property, you must have this permission.")
    async def create_charge_lease_transactions(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        lease_id: Annotated[int, Field(description="leaseId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/leases/{leaseId}/charges", path_params={"leaseId": lease_id}, query={}, body=body)

    @mcp.tool(name="get_listing_contact_by_id", description="[Listings] Retrieve a listing contact. Retrieves a specific listing contact. Required permission(s): Rentals > Listings - `View`")
    async def get_listing_contact_by_id(
        listing_contact_id: Annotated[int, Field(description="The listing contact identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/rentals/units/listingcontacts/{listingContactId}", path_params={"listingContactId": listing_contact_id}, query={}, body=None)

    @mcp.tool(name="update_listing_contact", description="[Listings] Update a listing contact. Update a listing contact. Note, at least one contact field (phone number, email or website) is required for the listing contact. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Rentals > Listings - `View` `Edit`")
    async def update_listing_contact(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        listing_contact_id: Annotated[int, Field(description="The listing contact identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/rentals/units/listingcontacts/{listingContactId}", path_params={"listingContactId": listing_contact_id}, query={}, body=body)

    @mcp.tool(name="get_user_role_by_id", description="[Administration] Retrieve a user role. Retrieve a specific user role. Required permission(s): Administration > User Roles - `View`")
    async def get_user_role_by_id(
        user_role_id: Annotated[int, Field(description="The user role identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/userroles/{userRoleId}", path_params={"userRoleId": user_role_id}, query={}, body=None)

    @mcp.tool(name="get_application_ledger_charge_by_id", description="[Application Transactions] Retrieve a charge. Retrieves a specific application charge. Required permission(s): Rentals > Lease Transactions - `View`")
    async def get_application_ledger_charge_by_id(
        application_id: Annotated[int, Field(description="applicationId")],
        transaction_id: Annotated[int, Field(description="transactionId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/applications/{applicationId}/charges/{transactionId}", path_params={"applicationId": application_id, "transactionId": transaction_id}, query={}, body=None)

    @mcp.tool(name="update_application_ledger_charge", description="[Application Transactions] Update a charge. Updates a charge on a specific application ledger. Required permission(s): Rentals > Lease transactions - `View` `Edit`")
    async def update_application_ledger_charge(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        application_id: Annotated[int, Field(description="applicationId")],
        transaction_id: Annotated[int, Field(description="transactionId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/applications/{applicationId}/charges/{transactionId}", path_params={"applicationId": application_id, "transactionId": transaction_id}, query={}, body=body)

    @mcp.tool(name="create_association_ownership_account", description="[Ownership Accounts] Create an ownership account. Creates an ownership account. Required permission(s): Associations > Ownership accounts - `View` `Edit` Associations > Owners - `View` `Edit`")
    async def create_association_ownership_account(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/associations/ownershipaccounts", path_params={}, query={}, body=body)

    @mcp.tool(name="get_ownership_account_charge_by_id", description="[Ownership Account Transactions] Retrieve a charge. Retrieves a specific ownership account ledger charge. Required permission(s): Associations > Ownership account transactions - `View`")
    async def get_ownership_account_charge_by_id(
        ownership_account_id: Annotated[int, Field(description="The ownership account identifier.")],
        charge_id: Annotated[int, Field(description="chargeId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/ownershipaccounts/{ownershipAccountId}/charges/{chargeId}", path_params={"ownershipAccountId": ownership_account_id, "chargeId": charge_id}, query={}, body=None)

    @mcp.tool(name="update_ownership_account_charge", description="[Ownership Account Transactions] Update a charge. Updates a charge. Required permission(s): Associations > Ownership account transactions - `View` `Edit`")
    async def update_ownership_account_charge(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        ownership_account_id: Annotated[int, Field(description="The ownership account identifier.")],
        charge_id: Annotated[int, Field(description="The charge identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/associations/ownershipaccounts/{ownershipAccountId}/charges/{chargeId}", path_params={"ownershipAccountId": ownership_account_id, "chargeId": charge_id}, query={}, body=body)

    @mcp.tool(name="get_charge_by_id", description="[Lease Transactions] Retrieve a charge. Retrieves a specific lease charge. Required permissions(s): Rentals > Lease transactions - `View`")
    async def get_charge_by_id(
        lease_id: Annotated[int, Field(description="leaseId")],
        charge_id: Annotated[int, Field(description="chargeId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/{leaseId}/charges/{chargeId}", path_params={"leaseId": lease_id, "chargeId": charge_id}, query={}, body=None)

    @mcp.tool(name="update_lease_charge", description="[Lease Transactions] Update a charge. Updates a charge. Required permission(s): Rentals > Lease transactions - `View` `Edit`")
    async def update_lease_charge(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        lease_id: Annotated[int, Field(description="leaseId")],
        charge_id: Annotated[int, Field(description="chargeId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/leases/{leaseId}/charges/{chargeId}", path_params={"leaseId": lease_id, "chargeId": charge_id}, query={}, body=body)

    @mcp.tool(name="get_lease_move_out_information_by_id", description="[Leases] Retrieve all move outs. Retrieves a list of move out dates for a given lease. Required permission(s): Rentals > Leases - `View` Rentals > Tenants - `View`")
    async def get_lease_move_out_information_by_id(
        lease_id: Annotated[int, Field(description="leaseId")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/{leaseId}/moveouts", path_params={"leaseId": lease_id}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_move_out_data", description="[Leases] Create a move out. Creates move out data for a single tenant on a given lease. Required permission(s): Rentals > Leases - `View` `Edit` Rentals > Tenants - `View` `Edit`")
    async def create_move_out_data(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        lease_id: Annotated[int, Field(description="leaseId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/leases/{leaseId}/moveouts", path_params={"leaseId": lease_id}, query={}, body=body)

    @mcp.tool(name="create_inactivate_rental_property", description="[Rental Properties] Inactivate a property. Inactivates a rental property and all associated units. Any associated property's owners that have no remaining active properties will be inactivated. Required permission(s): Rentals > Rental properties and units - `View` `Edit`")
    async def create_inactivate_rental_property(
        property_id: Annotated[int, Field(description="propertyId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/rentals/{propertyId}/inactivationrequest", path_params={"propertyId": property_id}, query={}, body=None)

    @mcp.tool(name="get_asset_service_history", description="[Inventory and Assets] Retrieve asset service history. Retrieves a list of service history records for the specified inventory asset. Required permission(s): Maintenance > Inventory and Assets - `View`")
    async def get_asset_service_history(
        inventory_asset_id: Annotated[int, Field(description="inventoryAssetId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/assetservicehistory/{inventoryAssetId}", path_params={"inventoryAssetId": inventory_asset_id}, query={}, body=None)

    @mcp.tool(name="create_asset_service_history", description="[Inventory and Assets] Creates an asset service history entry. Creates an asset service history entry for a given inventory asset. Required permission(s): Maintenance > Inventory and Assets - `View` `Edit`")
    async def create_asset_service_history(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        inventory_asset_id: Annotated[int, Field(description="inventoryAssetId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/assetservicehistory/{inventoryAssetId}", path_params={"inventoryAssetId": inventory_asset_id}, query={}, body=body)

    @mcp.tool(name="get_ownership_account_by_id", description="[Ownership Accounts] Retrieve an ownership account. Retrieves a specific ownership account. Required permission(s): Associations > Ownership accounts - `View`")
    async def get_ownership_account_by_id(
        ownership_account_id: Annotated[int, Field(description="The ownership account identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/ownershipaccounts/{ownershipAccountId}", path_params={"ownershipAccountId": ownership_account_id}, query={}, body=None)

    @mcp.tool(name="update_association_ownership_account", description="[Ownership Accounts] Update an ownership account. Updates an ownership account. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Associations > Ownership accounts - `View` `Edit`")
    async def update_association_ownership_account(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        ownership_account_id: Annotated[int, Field(description="ownershipAccountId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/associations/ownershipaccounts/{ownershipAccountId}", path_params={"ownershipAccountId": ownership_account_id}, query={}, body=body)

    @mcp.tool(name="get_lease_move_out_data_by_tenant_id", description="[Leases] Retrieve a move out. Retrieves move out data for a single tenant on a given lease. Required permission(s): Rentals > Leases - `View` Rentals > Tenants - `View`")
    async def get_lease_move_out_data_by_tenant_id(
        lease_id: Annotated[int, Field(description="leaseId")],
        tenant_id: Annotated[int, Field(description="tenantId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/{leaseId}/moveouts/{tenantId}", path_params={"leaseId": lease_id, "tenantId": tenant_id}, query={}, body=None)

    @mcp.tool(name="delete_undo_tenant_moveout", description="[Leases] Delete a move out. Deletes move out data for a tenant on a given lease. Required Permission(s): Rentals > Leases - `View` `Edit` Rentals > Tenants - `View`")
    async def delete_undo_tenant_moveout(
        lease_id: Annotated[int, Field(description="leaseId")],
        tenant_id: Annotated[int, Field(description="tenantId")],
    ) -> dict[str, Any]:
        return await client.raw_request("DELETE", "/v1/leases/{leaseId}/moveouts/{tenantId}", path_params={"leaseId": lease_id, "tenantId": tenant_id}, query={}, body=None)

    @mcp.tool(name="create_reactivate_rental_property", description="[Rental Properties] Reactivate a property. Reactivates a rental property and all associated units. Any inactive rental owners assigned to this property will also be reactivated. Required permission(s): Rentals > Rental properties and units - `View` `Edit`")
    async def create_reactivate_rental_property(
        property_id: Annotated[int, Field(description="propertyId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/rentals/{propertyId}/reactivationrequest", path_params={"propertyId": property_id}, query={}, body=None)

    @mcp.tool(name="get_asset_service_history_by_id", description="[Inventory and Assets] Retrieve an asset service history record. Retrieves a specific service history record for the specified inventory asset. Required permission(s): Maintenance > Inventory and Assets - `View`")
    async def get_asset_service_history_by_id(
        inventory_asset_id: Annotated[int, Field(description="inventoryAssetId")],
        asset_service_history_id: Annotated[int, Field(description="assetServiceHistoryId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/assetservicehistory/{inventoryAssetId}/{assetServiceHistoryId}", path_params={"inventoryAssetId": inventory_asset_id, "assetServiceHistoryId": asset_service_history_id}, query={}, body=None)

    @mcp.tool(name="get_all_association_owners", description="[Association Owners] Retrieve all owners. Retrieves a list of association owners. Required permission(s): Associations > Association owners and tenants - `View`")
    async def get_all_association_owners(
        name: Annotated[str | None, Field(description="Filters results to only records whose name *contains* the specified value.")] = None,
        phone: Annotated[str | None, Field(description="Filters results to only records whose phone number *contains* the specified value.")] = None,
        email: Annotated[str | None, Field(description="Filters results to only records whose email *contains* the specified value.")] = None,
        associationids: Annotated[list[int] | None, Field(description="Filters results to only records that belong to the specified set of association identifiers.")] = None,
        statuses: Annotated[list[str] | None, Field(description="Filters results to only records whose status is equal to the specified value.")] = None,
        createddatetimeto: Annotated[str | None, Field(description="Filters results to only records that were created before this date. Must be formatted as `YYYY-MM-DD`.")] = None,
        createddatetimefrom: Annotated[str | None, Field(description="Filters results to only records that were created after this date. Must be formatted as `YYYY-MM-DD`.")] = None,
        lastupdatedfrom: Annotated[str | None, Field(description="Filters results to any association owners that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
        lastupdatedto: Annotated[str | None, Field(description="Filters results to any association owners that were updated on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/owners", path_params={}, query={"name": name, "phone": phone, "email": email, "associationids": associationids, "statuses": statuses, "createddatetimeto": createddatetimeto, "createddatetimefrom": createddatetimefrom, "lastupdatedfrom": lastupdatedfrom, "lastupdatedto": lastupdatedto, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_ownership_account_ledger_payment", description="[Ownership Account Transactions] Create a payment. Creates a ledger payment. Required permission(s): Associations > Ownership account transactions - `View` `Edit`")
    async def create_ownership_account_ledger_payment(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        ownership_account_id: Annotated[int, Field(description="ownershipAccountId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/associations/ownershipaccounts/{ownershipAccountId}/payments", path_params={"ownershipAccountId": ownership_account_id}, query={}, body=body)

    @mcp.tool(name="get_rental_preferred_vendors", description="[Rental Properties] Retrieve all preferred vendors. Retrieves all preferred vendors. Required permission(s): Rentals > Rental properties and units - `View` Maintenance > Vendors - `View`")
    async def get_rental_preferred_vendors(
        property_id: Annotated[int, Field(description="propertyId")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/rentals/{propertyId}/vendors", path_params={"propertyId": property_id}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="update_rental_preferred_vendors", description="[Rental Properties] Update preferred vendors. Updates preferred vendors. Required permission(s): Rentals > Rental properties and units - `View` `Edit` Maintenance > Vendors - `View` `Edit`")
    async def update_rental_preferred_vendors(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        property_id: Annotated[int, Field(description="propertyId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/rentals/{propertyId}/vendors", path_params={"propertyId": property_id}, query={}, body=body)

    @mcp.tool(name="create_application_ledger_payment", description="[Application Transactions] Create a payment. Creates an application ledger payment. Required permission(s): Rentals > Lease transactions - `View` `Edit`")
    async def create_application_ledger_payment(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        application_id: Annotated[int, Field(description="The application unique identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/applications/{applicationId}/payments", path_params={"applicationId": application_id}, query={}, body=body)

    @mcp.tool(name="create_ownership_account_auto_allocated_payment", description="[Ownership Account Transactions] Create a payment (auto allocated). Creates a payment on the ownership account ledger. Note that the recorded payment will be automatically allocated to the general ledger accounts based on the payment allocation settings. These settings can be found under the Settings > Application Settings > Residents page in your account. If you'd like to specify the general ledger accounts the payment should apply to, please use the Create a payment endpoint. Required permission(s): Associations > Ownership account transactions - `View` `Edit`")
    async def create_ownership_account_auto_allocated_payment(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        ownership_account_id: Annotated[int, Field(description="ownershipAccountId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/associations/ownershipaccounts/{ownershipAccountId}/autoallocatedpayments", path_params={"ownershipAccountId": ownership_account_id}, query={}, body=body)

    @mcp.tool(name="create_payment", description="[Lease Transactions] Create a payment. Creates a lease ledger payment. Required permission(s): Rentals > Lease transactions - `View` `Edit`")
    async def create_payment(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        lease_id: Annotated[int, Field(description="The lease unique identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/leases/{leaseId}/payments", path_params={"leaseId": lease_id}, query={}, body=body)

    @mcp.tool(name="create_application_auto_allocated_payment", description="[Application Transactions] Create a payment (auto allocated). Creates a payment on the application ledger. Note that the recorded payment will be automatically allocated to the general ledger accounts based on the payment allocation settings. These settings can be found under the Settings > Application Settings > Residents page in your account. If you'd like to specify the GL accounts the payment should apply to, please use the Create a payment endpoint. Required permission(s): Rentals > Lease transactions - `View` `Edit`")
    async def create_application_auto_allocated_payment(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        application_id: Annotated[int, Field(description="The application unique identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/applications/{applicationId}/autoallocatedpayments", path_params={"applicationId": application_id}, query={}, body=body)

    @mcp.tool(name="get_all_asset_categories", description="[Inventory and Assets] Retrieve all asset categories. Retrieves a list of asset categories. Required permission(s): Maintenance > Inventory and Assets - `View`")
    async def get_all_asset_categories(
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/assetcategories", path_params={}, query={}, body=None)

    @mcp.tool(name="update_ownership_account_ledger_payment", description="[Ownership Account Transactions] Update a payment. Updates a ledger payment. Each line item must have a unique general ledger account identifier. PaymentMethod, Date, Memo, and the total Amount cannot be changed for payments with a PaymentMethod of `BuildiumEFT`, `BuildiumCC` or `RetailCash`. Required permission(s): Associations > Ownership account transactions - `View` `Edit`")
    async def update_ownership_account_ledger_payment(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        ownership_account_id: Annotated[int, Field(description="ownershipAccountId")],
        payment_id: Annotated[int, Field(description="paymentId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/associations/ownershipaccounts/{ownershipAccountId}/payments/{paymentId}", path_params={"ownershipAccountId": ownership_account_id, "paymentId": payment_id}, query={}, body=body)

    @mcp.tool(name="get_association_tenants", description="[Association Tenants] Retrieve all tenants. Retrieves a list of association tenants. Required permission(s): Associations > Association owners and tenants - `View`")
    async def get_association_tenants(
        name: Annotated[str | None, Field(description="Filters results to only records whose name *contains* the specified value.")] = None,
        phone: Annotated[str | None, Field(description="Filters results to only records whose phone number *contains* the specified value.")] = None,
        email: Annotated[str | None, Field(description="Filters results to only records whose email *contains* the specified value.")] = None,
        associationids: Annotated[list[int] | None, Field(description="Filters results to only records that belong to the specified set of association identifiers.")] = None,
        statuses: Annotated[list[str] | None, Field(description="Filters results to only records whose status is equal to the specified value.")] = None,
        createddatetimeto: Annotated[str | None, Field(description="Filters results to only records that were created before this date. Must be formatted as `YYYY-MM-DD`.")] = None,
        createddatetimefrom: Annotated[str | None, Field(description="Filters results to only records that were created after this date. Must be formatted as `YYYY-MM-DD`.")] = None,
        lastupdatedfrom: Annotated[str | None, Field(description="Filters results to any association owners that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
        lastupdatedto: Annotated[str | None, Field(description="Filters results to any association owners that were updated on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/tenants", path_params={}, query={"name": name, "phone": phone, "email": email, "associationids": associationids, "statuses": statuses, "createddatetimeto": createddatetimeto, "createddatetimefrom": createddatetimefrom, "lastupdatedfrom": lastupdatedfrom, "lastupdatedto": lastupdatedto, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_lease_auto_allocated_payment", description="[Lease Transactions] Create a payment (auto allocated). Creates a payment on the lease ledger. Note that the recorded payment will be automatically allocated to the general ledger accounts based on the payment allocation settings. These settings can be found under the Settings > Application Settings > Residents page in your account. If you'd like to specify the GL accounts the payment should apply to, please use the Create a payment endpoint. Required permission(s): Rentals > Lease transactions - `View` `Edit`")
    async def create_lease_auto_allocated_payment(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        lease_id: Annotated[int, Field(description="leaseId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/leases/{leaseId}/autoallocatedpayments", path_params={"leaseId": lease_id}, query={}, body=body)

    @mcp.tool(name="get_lease_notes", description="[Leases] Retrieve all notes. Retrieves all lease notes. Required permission(s): Rentals > Leases - `View`")
    async def get_lease_notes(
        lease_id: Annotated[int, Field(description="leaseId")],
        updateddatetimefrom: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        updateddatetimeto: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        lastupdatedbyuserid: Annotated[int | None, Field(description="Filters results to only notes that were last updated by the specified user identifier.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/{leaseId}/notes", path_params={"leaseId": lease_id}, query={"updateddatetimefrom": updateddatetimefrom, "updateddatetimeto": updateddatetimeto, "lastupdatedbyuserid": lastupdatedbyuserid, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_lease_note", description="[Leases] Create a note. Creates a lease note. Required permission(s): Rentals > Leases - `View` `Edit`")
    async def create_lease_note(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        lease_id: Annotated[int, Field(description="leaseId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/leases/{leaseId}/notes", path_params={"leaseId": lease_id}, query={}, body=body)

    @mcp.tool(name="update_application_ledger_payment", description="[Application Transactions] Update a payment. Updates an application ledger payment. Each line item must have a unique general ledger account identifier. PaymentMethod, Date, Memo, and the total Amount cannot be changed for payments with a PaymentMethod of `BuildiumEFT`, `BuildiumCC` or `RetailCash`. Required permission(s): Rentals > Lease transactions - `View` `Edit`")
    async def update_application_ledger_payment(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        application_id: Annotated[int, Field(description="The application unique identifier.")],
        transaction_id: Annotated[int, Field(description="transactionId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/applications/{applicationId}/payments/{transactionId}", path_params={"applicationId": application_id, "transactionId": transaction_id}, query={}, body=body)

    @mcp.tool(name="create_ownership_account_credit", description="[Ownership Account Transactions] Create a credit. Creates a ledger credit. Required permission(s): Associations > Ownership account transactions - `View` `Edit`")
    async def create_ownership_account_credit(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        ownership_account_id: Annotated[int, Field(description="ownershipAccountId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/associations/ownershipaccounts/{ownershipAccountId}/credits", path_params={"ownershipAccountId": ownership_account_id}, query={}, body=body)

    @mcp.tool(name="get_association_tenant_by_id", description="[Association Tenants] Retrieve a tenant. Retrieves a specific association tenant. Required permission(s): Associations > Association owners and tenants - `View`")
    async def get_association_tenant_by_id(
        tenant_id: Annotated[int, Field(description="The tenant identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/tenants/{tenantId}", path_params={"tenantId": tenant_id}, query={}, body=None)

    @mcp.tool(name="get_inventory_storages", description="[Inventory and Assets] Retrieve all inventory storages. Retrieves a list of inventory storages. Required permission(s): Maintenance > Inventory and Assets - `View`")
    async def get_inventory_storages(
        entitytype: Annotated[str | None, Field(description="Filters results to inventory storages associated with the specified entity type.")] = None,
        entityid: Annotated[int | None, Field(description="Filters results to inventory storages associated with the specified entity identifier.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/inventorystorages", path_params={}, query={"entitytype": entitytype, "entityid": entityid}, body=None)

    @mcp.tool(name="get_lease_note_by_note_id", description="[Leases] Retrieve a note. Retrieves a lease note. Required permission(s): Rentals > Leases - `View`")
    async def get_lease_note_by_note_id(
        lease_id: Annotated[int, Field(description="leaseId")],
        note_id: Annotated[int, Field(description="noteId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/{leaseId}/notes/{noteId}", path_params={"leaseId": lease_id, "noteId": note_id}, query={}, body=None)

    @mcp.tool(name="update_lease_note", description="[Leases] Update a note. Updates a lease note. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Rentals > Leases - `View` `Edit`")
    async def update_lease_note(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        lease_id: Annotated[int, Field(description="leaseId")],
        note_id: Annotated[int, Field(description="noteId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/leases/{leaseId}/notes/{noteId}", path_params={"leaseId": lease_id, "noteId": note_id}, query={}, body=body)

    @mcp.tool(name="update_lease_ledger_payment", description="[Lease Transactions] Update a payment. Updates a ledger payment. Each line item must have a unique general ledger account identifier. PaymentMethod, Date, Memo, and the total Amount cannot be changed for payments with a PaymentMethod of `BuildiumEFT`, `BuildiumCC` or `RetailCash`. Required permission(s): Rentals > Lease transactions - `View` `Edit`")
    async def update_lease_ledger_payment(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        lease_id: Annotated[int, Field(description="leaseId")],
        payment_id: Annotated[int, Field(description="paymentId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/leases/{leaseId}/payments/{paymentId}", path_params={"leaseId": lease_id, "paymentId": payment_id}, query={}, body=body)

    @mcp.tool(name="create_lease_reverse_payment", description="[Lease Transactions] Create a payment reversal. Reverses a lease ledger payment. Note, this action can only be taken on a payment that has been deposited. Required permission(s): Rentals > Lease transactions - `View` `Edit` Accounting > Bank Accounts - `View` `Edit`")
    async def create_lease_reverse_payment(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        lease_id: Annotated[int, Field(description="The lease unique identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/leases/{leaseId}/reversepayments", path_params={"leaseId": lease_id}, query={}, body=body)

    @mcp.tool(name="create_application_ledger_reverse_payment", description="[Application Transactions] Create a payment reversal. Reverses an application ledger payment. Note, this action can only be taken on a payment that has been deposited. Required permission(s): Rentals > Lease transactions - `View` `Edit` Accounting > Bank Accounts - `View` `Edit`")
    async def create_application_ledger_reverse_payment(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        application_id: Annotated[int, Field(description="The application unique identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/applications/{applicationId}/reversepayments", path_params={"applicationId": application_id}, query={}, body=body)

    @mcp.tool(name="get_ownership_account_refund_by_id", description="[Ownership Account Transactions] Retrieve a refund. Retrieves a refund. Required permission(s): Accounting > Bank Accounts - `View`")
    async def get_ownership_account_refund_by_id(
        ownership_account_id: Annotated[int, Field(description="ownershipAccountId")],
        refund_id: Annotated[int, Field(description="refundId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/ownershipaccounts/{ownershipAccountId}/refunds/{refundId}", path_params={"ownershipAccountId": ownership_account_id, "refundId": refund_id}, query={}, body=None)

    @mcp.tool(name="get_lease_ledger_refund_by_id", description="[Lease Transactions] Retrieve a refund. Retrieves a refund. Required permission(s): Accounting > Bank Accounts - `View`")
    async def get_lease_ledger_refund_by_id(
        lease_id: Annotated[int, Field(description="leaseId")],
        refund_id: Annotated[int, Field(description="refundId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/{leaseId}/refunds/{refundId}", path_params={"leaseId": lease_id, "refundId": refund_id}, query={}, body=None)

    @mcp.tool(name="get_application_ledger_refund_by_id", description="[Application Transactions] Retrieve a refund. Retrieves a specific application refund. Required permission(s): Rentals > Lease transactions - `View`")
    async def get_application_ledger_refund_by_id(
        application_id: Annotated[int, Field(description="applicationId")],
        transaction_id: Annotated[int, Field(description="transactionId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/applications/{applicationId}/refunds/{transactionId}", path_params={"applicationId": application_id, "transactionId": transaction_id}, query={}, body=None)

    @mcp.tool(name="create_ownership_account_refund", description="[Ownership Account Transactions] Create a refund. Creates a refund. Required permission(s): Accounting > Bank Accounts - `View` `Edit`")
    async def create_ownership_account_refund(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        ownership_account_id: Annotated[int, Field(description="ownershipAccountId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/associations/ownershipaccounts/{ownershipAccountId}/refunds", path_params={"ownershipAccountId": ownership_account_id}, query={}, body=body)

    @mcp.tool(name="create_lease_ledger_refund", description="[Lease Transactions] Create a refund. Creates a refund. Required permission(s): Accounting > Bank Accounts - `View` `Edit`")
    async def create_lease_ledger_refund(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        lease_id: Annotated[int, Field(description="leaseId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/leases/{leaseId}/refunds", path_params={"leaseId": lease_id}, query={}, body=body)

    @mcp.tool(name="create_application_ledger_refund", description="[Application Transactions] Create a refund. Creates a refund for a specific application. Required permission(s): Rentals > Lease transactions - `View` `Edit`")
    async def create_application_ledger_refund(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        application_id: Annotated[int, Field(description="applicationId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/applications/{applicationId}/refunds", path_params={"applicationId": application_id}, query={}, body=body)

    @mcp.tool(name="create_ownership_account_deposit_withholding", description="[Ownership Account Transactions] Create a deposit withholding. Withholds an association owner deposit by reallocating the funds from a liability account to an income account to cover an expense(s). Required permission(s): Associations > Ownership account transactions - `View` `Edit` Accounting > General Ledger Accounts - `View`")
    async def create_ownership_account_deposit_withholding(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        ownership_account_id: Annotated[int, Field(description="ownershipAccountId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/associations/ownershipaccounts/{ownershipAccountId}/applieddeposits", path_params={"ownershipAccountId": ownership_account_id}, query={}, body=body)

    @mcp.tool(name="create_lease_credit", description="[Lease Transactions] Create a credit. Creates a lease ledger credit. Required permission(s): Rentals > Lease transactions - `View` `Edit`")
    async def create_lease_credit(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        lease_id: Annotated[int, Field(description="The lease unique identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/leases/{leaseId}/credits", path_params={"leaseId": lease_id}, query={}, body=body)

    @mcp.tool(name="get_all_lease_renewals_for_all_properties", description="[Leases] Retrieve all upcoming renewals. Retrieves all upcoming lease renewals across all rental properties. Required permission(s): Rentals > Leases - `View`")
    async def get_all_lease_renewals_for_all_properties(
        esignaturestatuses: Annotated[list[str], Field(description="Filters result to any lease renewal with an esignature status that matches the given statuses.")],
        propertyids: Annotated[list[int] | None, Field(description="Filters results to only include leases whose unit belongs to the specified set of property ids.")] = None,
        rentalownerids: Annotated[list[int] | None, Field(description="Filters results to any lease whose unit belongs to a property with rental owner in the specified set of rental owner ids.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/renewals", path_params={}, query={"propertyids": propertyids, "rentalownerids": rentalownerids, "esignaturestatuses": esignaturestatuses, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="update_ownership_account_deposit_withholding", description="[Ownership Account Transactions] Update a deposit withholding. Updates an ownership account deposit withholding. Required permission(s): Associations > Ownership account transactions - `View` `Edit` Accounting > General Ledger Accounts - `View`")
    async def update_ownership_account_deposit_withholding(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        ownership_account_id: Annotated[int, Field(description="ownershipAccountId")],
        deposit_id: Annotated[int, Field(description="depositId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/associations/ownershipaccounts/{ownershipAccountId}/applieddeposits/{depositId}", path_params={"ownershipAccountId": ownership_account_id, "depositId": deposit_id}, query={}, body=body)

    @mcp.tool(name="create_lease_ledger_deposit_withholding", description="[Lease Transactions] Create a deposit withholding. Withholds a resident deposit by reallocating the funds from a liability account to an income account to cover an expense(s). Required permission(s): Rentals > Lease Ledger - `View` `Edit` Accounting > General Ledger Accounts - `View`")
    async def create_lease_ledger_deposit_withholding(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        lease_id: Annotated[int, Field(description="leaseId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/leases/{leaseId}/applieddeposits", path_params={"leaseId": lease_id}, query={}, body=body)

    @mcp.tool(name="get_all_lease_renewals", description="[Leases] Retrieve all renewals. Retrieves all renewals for a specific a lease. Required permission(s): Rentals > Leases - `View`")
    async def get_all_lease_renewals(
        lease_id: Annotated[int, Field(description="leaseId")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/{leaseId}/renewals", path_params={"leaseId": lease_id}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_lease_renewal", description="[Leases] Create a lease renewal. Creates a lease renewal. Required permission(s): Rentals > Leases - `View` `Edit`")
    async def create_lease_renewal(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        lease_id: Annotated[int, Field(description="leaseId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/leases/{leaseId}/renewals", path_params={"leaseId": lease_id}, query={}, body=body)

    @mcp.tool(name="get_association_recurring_transaction", description="[Ownership Account Transactions] Retrieve all recurring transactions. Retrieves all recurring transactions for an ownership account. Required permission(s): Associations > Ownership account transactions - `View`")
    async def get_association_recurring_transaction(
        ownership_account_id: Annotated[int, Field(description="ownershipAccountId")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/ownershipaccounts/{ownershipAccountId}/recurringtransactions", path_params={"ownershipAccountId": ownership_account_id}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="update_deposit_withholding", description="[Lease Transactions] Update a deposit withholding. Updates a resident deposit withholding. Required permission(s): Rentals > Lease Ledger - `View` `Edit` Accounting > General Ledger Accounts - `View`")
    async def update_deposit_withholding(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        lease_id: Annotated[int, Field(description="leaseId")],
        deposit_id: Annotated[int, Field(description="depositId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/leases/{leaseId}/applieddeposits/{depositId}", path_params={"leaseId": lease_id, "depositId": deposit_id}, query={}, body=body)

    @mcp.tool(name="get_lease_renewal_by_id", description="[Leases] Retrieve a renewal. Retrieves a specific renewal for a given lease. Required permission(s): Rentals > Leases - `View`")
    async def get_lease_renewal_by_id(
        lease_id: Annotated[int, Field(description="leaseId")],
        renewal_id: Annotated[int, Field(description="renewalId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/{leaseId}/renewals/{renewalId}", path_params={"leaseId": lease_id, "renewalId": renewal_id}, query={}, body=None)

    @mcp.tool(name="get_lease_recurring_transactions", description="[Lease Transactions] Retrieve all recurring transactions. Retrieves all recurring transactions for a given lease. Required permission(s): Rentals > Lease transactions - `View`")
    async def get_lease_recurring_transactions(
        lease_id: Annotated[int, Field(description="leaseId")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/{leaseId}/recurringtransactions", path_params={"leaseId": lease_id}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_account_info", description="[Administration] Retrieve account info. Retrieves information related to the Buildium account. Required permission(s): Administration > Account Information - `View`")
    async def get_account_info(
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/administration/account", path_params={}, query={}, body=None)

    @mcp.tool(name="get_accounting_lock_period_settings", description="[Administration] Retrieve accounting lock periods. Retrieves accounting lock periods. Required permission(s): Administration > Application Settings - `View`")
    async def get_accounting_lock_period_settings(
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/administration/accountinglockperiod", path_params={}, query={}, body=None)

    @mcp.tool(name="get_global_partial_payment_settings", description="[Administration] Retrieve the partial payment settings for residents. Retrieves the partial payment settings for residents. Required permission(s): Administration > Application Settings - `View`")
    async def get_global_partial_payment_settings(
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/administration/residentsettings/partialpaymentsettings", path_params={}, query={}, body=None)

    @mcp.tool(name="update_patch_global_partial_payment_settings", description="[Administration] Update the partial payment settings for residents. Updates the partial payment settings for residents. Required permission(s): Administration > Application Settings - `View` `Edit`")
    async def update_patch_global_partial_payment_settings(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
    ) -> dict[str, Any]:
        return await client.raw_request("PATCH", "/v1/administration/residentsettings/partialpaymentsettings", path_params={}, query={}, body=body)

    @mcp.tool(name="get_all_applicant_notes", description="[Applicants] Retrieve all applicant notes. Retrieves all applicant notes. Required permission(s): Rentals > Applicants - `View`")
    async def get_all_applicant_notes(
        applicant_id: Annotated[int, Field(description="applicantId")],
        updateddatetimefrom: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        updateddatetimeto: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        lastupdatedbyuserid: Annotated[int | None, Field(description="Filters results to only notes that were last updated by the specified user identifier.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/applicants/{applicantId}/notes", path_params={"applicantId": applicant_id}, query={"updateddatetimefrom": updateddatetimefrom, "updateddatetimeto": updateddatetimeto, "lastupdatedbyuserid": lastupdatedbyuserid, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_applicant_note", description="[Applicants] Create an applicant note. Creates an applicant note. Required permission(s): Rentals > Applicants - `View` `Edit`")
    async def create_applicant_note(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        applicant_id: Annotated[int, Field(description="applicantId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/applicants/{applicantId}/notes", path_params={"applicantId": applicant_id}, query={}, body=body)

    @mcp.tool(name="get_applicant_note_by_id", description="[Applicants] Retrieve an applicant note. Retrieves an applicant note. Required permission(s): Rentals > Applicants - `View`")
    async def get_applicant_note_by_id(
        applicant_id: Annotated[int, Field(description="applicantId")],
        note_id: Annotated[int, Field(description="noteId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/applicants/{applicantId}/notes/{noteId}", path_params={"applicantId": applicant_id, "noteId": note_id}, query={}, body=None)

    @mcp.tool(name="get_applicant_group_by_id", description="[Applicants] Retrieve an applicant group. Retrieves an applicant group. Required permission(s): Rentals > Applicants - `View`")
    async def get_applicant_group_by_id(
        applicant_group_id: Annotated[int, Field(description="applicantGroupId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/applicants/groups/{applicantGroupId}", path_params={"applicantGroupId": applicant_group_id}, query={}, body=None)

    @mcp.tool(name="get_applicant_group_notes", description="[Applicants] Retrieve all applicant group notes. Retrieves all applicant group notes. Required permission(s): Rentals > Applicants - `View`")
    async def get_applicant_group_notes(
        applicant_group_id: Annotated[int, Field(description="applicantGroupId")],
        updateddatetimefrom: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        updateddatetimeto: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        lastupdatedbyuserid: Annotated[int | None, Field(description="Filters results to only notes that were last updated by the specified user identifier.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/applicants/groups/{applicantGroupId}/notes", path_params={"applicantGroupId": applicant_group_id}, query={"updateddatetimefrom": updateddatetimefrom, "updateddatetimeto": updateddatetimeto, "lastupdatedbyuserid": lastupdatedbyuserid, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_application_group_note", description="[Applicants] Create an applicant group note. Creates an applicant group note. Required permission(s): Rentals > Applicants - `View` `Edit`")
    async def create_application_group_note(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        applicant_group_id: Annotated[int, Field(description="applicantGroupId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/applicants/groups/{applicantGroupId}/notes", path_params={"applicantGroupId": applicant_group_id}, query={}, body=body)

    @mcp.tool(name="get_applicant_group_note_by_note_id", description="[Applicants] Retrieve an applicant group note. Retrieves an applicant group note. Required permission(s): Rentals > Applicants - `View`")
    async def get_applicant_group_note_by_note_id(
        applicant_group_id: Annotated[int, Field(description="applicantGroupId")],
        note_id: Annotated[int, Field(description="noteId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/applicants/groups/{applicantGroupId}/notes/{noteId}", path_params={"applicantGroupId": applicant_group_id, "noteId": note_id}, query={}, body=None)

    @mcp.tool(name="update_application_group_note", description="[Applicants] Update an applicant group note. Updates an applicant group note. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Rentals > Applicants - `View` `Edit`")
    async def update_application_group_note(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        applicant_group_id: Annotated[int, Field(description="applicantGroupId")],
        note_id: Annotated[int, Field(description="noteId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/applicants/groups/{applicantGroupId}/notes/{noteId}", path_params={"applicantGroupId": applicant_group_id, "noteId": note_id}, query={}, body=body)

    @mcp.tool(name="create_board_member", description="[Board Members] Create a board member. Creates a board member for a given association. Required permission(s): Associations > Association owners and tenants - `View` `Edit`")
    async def create_board_member(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        association_id: Annotated[int, Field(description="associationId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/associations/{associationId}/boardmembers", path_params={"associationId": association_id}, query={}, body=body)

    @mcp.tool(name="get_association_board_member_by_id", description="[Board Members] Retrieve a board member. Retrieves an association board member. Required permission(s): Associations > Association owners and tenants - `View`")
    async def get_association_board_member_by_id(
        association_id: Annotated[int, Field(description="associationId")],
        board_member_id: Annotated[int, Field(description="boardMemberId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/{associationId}/boardmembers/{boardMemberId}", path_params={"associationId": association_id, "boardMemberId": board_member_id}, query={}, body=None)

    @mcp.tool(name="update_board_member", description="[Board Members] Update a board member. Updates a board member for a given association. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Associations > Association owners and tenants - `View` `Edit`")
    async def update_board_member(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        association_id: Annotated[int, Field(description="associationId")],
        board_member_id: Annotated[int, Field(description="boardMemberId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/associations/{associationId}/boardmembers/{boardMemberId}", path_params={"associationId": association_id, "boardMemberId": board_member_id}, query={}, body=body)

    @mcp.tool(name="delete_board_member", description="[Board Members] Delete a board member. Deletes a board member. Note, this is a hard delete from the database and data can not be restored. Required permission(s): Associations > Association owners and tenants - `View` `Edit` `Delete`")
    async def delete_board_member(
        association_id: Annotated[int, Field(description="associationId")],
        board_member_id: Annotated[int, Field(description="boardMemberId")],
    ) -> dict[str, Any]:
        return await client.raw_request("DELETE", "/v1/associations/{associationId}/boardmembers/{boardMemberId}", path_params={"associationId": association_id, "boardMemberId": board_member_id}, query={}, body=None)

    @mcp.tool(name="get_e_pay_settings_for_association_by_id", description="[Associations] Retrieve ePay settings. Retrieves ePay settings for an association. Required permission(s): Associations > Associations and units - `View`")
    async def get_e_pay_settings_for_association_by_id(
        association_id: Annotated[int, Field(description="associationId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/{associationId}/epaysettings", path_params={"associationId": association_id}, query={}, body=None)

    @mcp.tool(name="update_e_pay_settings_for_association", description="[Associations] Update ePay settings. Updates ePay settings for an association. Required permission(s): Associations > Associations and units - `View` `Edit`")
    async def update_e_pay_settings_for_association(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        association_id: Annotated[int, Field(description="associationId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/associations/{associationId}/epaysettings", path_params={"associationId": association_id}, query={}, body=body)

    @mcp.tool(name="create_inactivate_association", description="[Associations] Inactivate an association. Inactivates an association along with associated units and ownership accounts. Required permission(s): Associations > Associations and units - `View` `Edit`")
    async def create_inactivate_association(
        association_id: Annotated[int, Field(description="associationId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/associations/{associationId}/inactivationrequest", path_params={"associationId": association_id}, query={}, body=None)

    @mcp.tool(name="get_meter_readings_for_association", description="[Association Meter Readings] Retrieve all meter readings. Retrieves all meter readings for an association. Required permission(s): Associations > Associations and units - `View`")
    async def get_meter_readings_for_association(
        association_id: Annotated[int, Field(description="associationId")],
        readingdatefrom: Annotated[str, Field(description="Filters results to any meter readings whose entry date that is greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD. The maximum date range is 365 days.")],
        readingdateto: Annotated[str, Field(description="Filters results to any meter readings whose entry date is less than or equal to the specified value. The value must be formatted as YYYY-MM-DD. The maximum date range is 365 days.")],
        metertypes: Annotated[list[str] | None, Field(description="Filters results to the specified meter types.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/{associationId}/meterreadings", path_params={"associationId": association_id}, query={"readingdatefrom": readingdatefrom, "readingdateto": readingdateto, "metertypes": metertypes, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_association_meter_reading_details_async", description="[Association Meter Readings] Retrieve all meter reading details. Retrieves all meter reading details for an association. Required permission(s): Associations > Associations and units - `View`")
    async def get_association_meter_reading_details_async(
        association_id: Annotated[int, Field(description="associationId")],
        readingdate: Annotated[str, Field(description="Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD.")],
        metertype: Annotated[str, Field(description="Filters results to the specified meter type.")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/{associationId}/meterreadings/summary", path_params={"associationId": association_id}, query={"readingdate": readingdate, "metertype": metertype}, body=None)

    @mcp.tool(name="update_upsert_association_meter_reading_details_async", description="[Association Meter Readings] Create/Update meter reading details. This endpoint can be used to both create and update a meter reading detail for an association. There can only be one meter reading detail for a given combination of MeterType and ReadingDate for an association If you are updating an existing meter reading detail, use the query parameters to specify the existing meter reading detail to update. If you are creating a new meter reading detail, do not pass any query parameters. When adding a new item to the Details array, leave out the `Id` field. When updating an existing item in the Details array, the `Id` field of the existing item must be included. Required permission(s): Associations > Associations and units - `View` `Edit`")
    async def update_upsert_association_meter_reading_details_async(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        association_id: Annotated[int, Field(description="associationId")],
        readingdate: Annotated[str | None, Field(description="Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD.")] = None,
        metertype: Annotated[str | None, Field(description="Filters results to the specified meter type.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/associations/{associationId}/meterreadings/summary", path_params={"associationId": association_id}, query={"readingdate": readingdate, "metertype": metertype}, body=body)

    @mcp.tool(name="delete_meter_reading_details_for_association", description="[Association Meter Readings] Delete meter reading details for a given date. Delete meter reading details for an association for a given date. Required permission(s): Associations > Ownership account transactions - `View` `Edit` `Delete`")
    async def delete_meter_reading_details_for_association(
        association_id: Annotated[int, Field(description="associationId")],
        readingdate: Annotated[str, Field(description="Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD.")],
        metertype: Annotated[str, Field(description="Filters results to the specified meter type.")],
    ) -> dict[str, Any]:
        return await client.raw_request("DELETE", "/v1/associations/{associationId}/meterreadings/summary", path_params={"associationId": association_id}, query={"readingdate": readingdate, "metertype": metertype}, body=None)

    @mcp.tool(name="get_association_notes", description="[Associations] Retrieve all notes. Retrieves all notes. Required permission(s): Associations > Associations and units - `View`")
    async def get_association_notes(
        association_id: Annotated[int, Field(description="associationId")],
        updateddatetimefrom: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        updateddatetimeto: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        lastupdatedbyuserid: Annotated[int | None, Field(description="Filters results to only notes that were last updated by the specified user identifier.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/{associationId}/notes", path_params={"associationId": association_id}, query={"updateddatetimefrom": updateddatetimefrom, "updateddatetimeto": updateddatetimeto, "lastupdatedbyuserid": lastupdatedbyuserid, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_association_note", description="[Associations] Create a note. Creates a note. Required permission(s): Associations > Associations and units - `View` `Edit`")
    async def create_association_note(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        association_id: Annotated[int, Field(description="associationId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/associations/{associationId}/notes", path_params={"associationId": association_id}, query={}, body=body)

    @mcp.tool(name="get_association_note_by_note_id", description="[Associations] Retrieve a note. Retrieves a note. Required permission(s): Associations > Associations and units - `View`")
    async def get_association_note_by_note_id(
        association_id: Annotated[int, Field(description="associationId")],
        note_id: Annotated[int, Field(description="noteId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/{associationId}/notes/{noteId}", path_params={"associationId": association_id, "noteId": note_id}, query={}, body=None)

    @mcp.tool(name="update_association_note", description="[Associations] Update a note. Updates a note. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Associations > Associations and units - `View` `Edit`")
    async def update_association_note(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        association_id: Annotated[int, Field(description="associationId")],
        note_id: Annotated[int, Field(description="noteId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/associations/{associationId}/notes/{noteId}", path_params={"associationId": association_id, "noteId": note_id}, query={}, body=body)

    @mcp.tool(name="create_reactivate_association", description="[Associations] Reactivate an association. Reactivates an association along with associated units and ownership accounts. Required permission(s): Associations > Associations and units - `View` `Edit`")
    async def create_reactivate_association(
        association_id: Annotated[int, Field(description="associationId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/associations/{associationId}/reactivationrequest", path_params={"associationId": association_id}, query={}, body=None)

    @mcp.tool(name="get_association_preferred_vendors", description="[Associations] Retrieve all preferred vendors. Retrieves all preferred vendors. Required permission(s): Associations > Associations and units - `View` Maintenance > Vendors - `View`")
    async def get_association_preferred_vendors(
        association_id: Annotated[int, Field(description="associationId")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/{associationId}/vendors", path_params={"associationId": association_id}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="update_association_preferred_vendors", description="[Associations] Update preferred vendors. Updates preferred vendors. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Associations > Associations and units - `View` `Edit` Maintenance > Vendors - `View` `Edit`")
    async def update_association_preferred_vendors(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        association_id: Annotated[int, Field(description="associationId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/associations/{associationId}/vendors", path_params={"associationId": association_id}, query={}, body=body)

    @mcp.tool(name="get_association_appliances", description="[Appliances] Retrieve all appliances. **\u26a0 Deprecated:** This endpoint is deprecated and will start returning **410 Gone** on 2026-10-19. Use `GET /v1/inventoryassets` instead. Appliances have moved to the new Inventory & Assets API. Retrieves all association appliances. Required permission(s): Associations > Associations and units - `View`")
    async def get_association_appliances(
        associationids: Annotated[list[int] | None, Field(description="Filters results to appliances associated to any of the specified association identifiers.")] = None,
        unitids: Annotated[list[int] | None, Field(description="Filters results to appliances associated to any of the specified association unit identifiers.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/appliances", path_params={}, query={"associationids": associationids, "unitids": unitids, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_association_appliance", description="[Appliances] Create an appliance. **\u26a0 Deprecated:** This endpoint is deprecated and will start returning **410 Gone** on 2026-10-19. Use `POST /v1/inventoryasset` instead. Appliances have moved to the new Inventory & Assets API. Creates an association appliance. Required permission(s): Associations > Associations and units - `View` `Edit`")
    async def create_association_appliance(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/associations/appliances", path_params={}, query={}, body=body)

    @mcp.tool(name="get_association_appliance_by_id", description="[Appliances] Retrieve an appliance. **\u26a0 Deprecated:** This endpoint is deprecated and will start returning **410 Gone** on 2026-10-19. Use `GET /v1/inventoryasset/{inventoryAssetId}` instead. Appliances have moved to the new Inventory & Assets API. Retrieves an association appliance by id. Required permission(s): Associations > Associations and units - `View`")
    async def get_association_appliance_by_id(
        appliance_id: Annotated[int, Field(description="applianceId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/appliances/{applianceId}", path_params={"applianceId": appliance_id}, query={}, body=None)

    @mcp.tool(name="update_association_appliance", description="[Appliances] Update an appliance. **\u26a0 Deprecated:** This endpoint is deprecated and will start returning **410 Gone** on 2026-10-19. Use `PUT /v1/inventoryasset/{inventoryAssetId}` instead. Appliances have moved to the new Inventory & Assets API. Updates an association appliance. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Associations > Associations and units - `View` `Edit`")
    async def update_association_appliance(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        appliance_id: Annotated[int, Field(description="applianceId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/associations/appliances/{applianceId}", path_params={"applianceId": appliance_id}, query={}, body=body)

    @mcp.tool(name="delete_association_appliances", description="[Appliances] Delete an appliance. **\u26a0 Deprecated:** This endpoint is deprecated and will start returning **410 Gone** on 2026-10-19. Use `DELETE /v1/inventoryasset/{inventoryAssetId}` instead. Appliances have moved to the new Inventory & Assets API. Deletes an associations appliance. Required permission(s): Associations > Associations and units - `View` `Edit`")
    async def delete_association_appliances(
        appliance_id: Annotated[int, Field(description="applianceId")],
    ) -> dict[str, Any]:
        return await client.raw_request("DELETE", "/v1/associations/appliances/{applianceId}", path_params={"applianceId": appliance_id}, query={}, body=None)

    @mcp.tool(name="get_all_association_appliance_service_history", description="[Appliances] Retrieve all service history. **\u26a0 Deprecated:** This endpoint is deprecated and will start returning **410 Gone** on 2026-10-19. Use `GET /v1/assetservicehistory/{inventoryAssetId}` instead. Appliances have moved to the new Inventory & Assets API. Retrieves all of the service history records for an appliance. Required permission(s): Associations > Associations and units - `View`")
    async def get_all_association_appliance_service_history(
        appliance_id: Annotated[int, Field(description="applianceId")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/appliances/{applianceId}/servicehistory", path_params={"applianceId": appliance_id}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_association_appliance_service_history", description="[Appliances] Create a service history. **\u26a0 Deprecated:** This endpoint is deprecated and will start returning **410 Gone** on 2026-10-19. Use `POST /v1/assetservicehistory/{inventoryAssetId}` instead. Appliances have moved to the new Inventory & Assets API. Creates a service history for an appliance. Required permission(s): Associations > Associations and units - `View` `Edit`")
    async def create_association_appliance_service_history(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        appliance_id: Annotated[int, Field(description="applianceId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/associations/appliances/{applianceId}/servicehistory", path_params={"applianceId": appliance_id}, query={}, body=body)

    @mcp.tool(name="get_association_appliance_service_history_by_id", description="[Appliances] Retrieve a service history. **\u26a0 Deprecated:** This endpoint is deprecated and will start returning **410 Gone** on 2026-10-19. Use `GET /v1/assetservicehistory/{inventoryAssetId}/{assetServiceHistoryId}` instead. Appliances have moved to the new Inventory & Assets API. Retrieves a specific service history record for a given appliance. Required permission(s): Associations > Associations and units - `View`")
    async def get_association_appliance_service_history_by_id(
        appliance_id: Annotated[int, Field(description="applianceId")],
        service_history_id: Annotated[int, Field(description="serviceHistoryId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/appliances/{applianceId}/servicehistory/{serviceHistoryId}", path_params={"applianceId": appliance_id, "serviceHistoryId": service_history_id}, query={}, body=None)

    @mcp.tool(name="get_bank_lock_box_data", description="[Associations] Retrieve all association bank lockbox data. Retrieves all association bank lockbox data. Required permission(s): Associations > Associations and units - `View`")
    async def get_bank_lock_box_data(
        associationids: Annotated[list[int] | None, Field(description="Filters results to only include Associations with matching IDs")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/banklockboxdata", path_params={}, query={"associationids": associationids, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_association_owner_notes", description="[Association Owners] Retrieve all notes. Retrieves all association owner notes. Required permission(s): Associations > Association owners and tenants - `View`")
    async def get_association_owner_notes(
        owner_id: Annotated[int, Field(description="ownerId")],
        updateddatetimefrom: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        updateddatetimeto: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        lastupdatedbyuserid: Annotated[int | None, Field(description="Filters results to only notes that were last updated by the specified user identifier.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/owners/{ownerId}/notes", path_params={"ownerId": owner_id}, query={"updateddatetimefrom": updateddatetimefrom, "updateddatetimeto": updateddatetimeto, "lastupdatedbyuserid": lastupdatedbyuserid, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_association_owner_note", description="[Association Owners] Create a note. Creates an association owner note. Required permission(s): Associations > Association owners and tenants - `View` `Edit`")
    async def create_association_owner_note(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        owner_id: Annotated[int, Field(description="ownerId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/associations/owners/{ownerId}/notes", path_params={"ownerId": owner_id}, query={}, body=body)

    @mcp.tool(name="get_association_owner_note_by_note_id", description="[Association Owners] Retrieve a note. Retrieves an association owner note. Required permission(s): Associations > Association owners and tenants - `View`")
    async def get_association_owner_note_by_note_id(
        owner_id: Annotated[int, Field(description="ownerId")],
        note_id: Annotated[int, Field(description="noteId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/owners/{ownerId}/notes/{noteId}", path_params={"ownerId": owner_id, "noteId": note_id}, query={}, body=None)

    @mcp.tool(name="update_association_owner_note", description="[Association Owners] Update a note. Updates an association owner note. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Associations > Association owners and tenants - `View` `Edit`")
    async def update_association_owner_note(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        owner_id: Annotated[int, Field(description="ownerId")],
        note_id: Annotated[int, Field(description="noteId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/associations/owners/{ownerId}/notes/{noteId}", path_params={"ownerId": owner_id, "noteId": note_id}, query={}, body=body)

    @mcp.tool(name="get_unit_occupancy_statuses_for_association_owner", description="[Association Owners] Retrieve all occupancy statuses. Retrieves the occupancy status for all of the units owned by the association owner. Required permission(s): Associations > Association owners and tenants - `View` Associations > Ownership Accounts - `View`")
    async def get_unit_occupancy_statuses_for_association_owner(
        owner_id: Annotated[int, Field(description="ownerId")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/owners/{ownerId}/units", path_params={"ownerId": owner_id}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_unit_occupancy_statuses_by_id_for_association_owner", description="[Association Owners] Retrieve an occupancy status. Retrieves the owner occupancy status for an association unit. Required permission(s): Associations > Association owners and tenants - `View` Associations > Ownership Accounts - `View`")
    async def get_unit_occupancy_statuses_by_id_for_association_owner(
        owner_id: Annotated[int, Field(description="ownerId")],
        unit_id: Annotated[int, Field(description="unitId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/owners/{ownerId}/units/{unitId}", path_params={"ownerId": owner_id, "unitId": unit_id}, query={}, body=None)

    @mcp.tool(name="update_association_owner_occupancy_status", description="[Association Owners] Update occupancy status. Updates whether a unit is occupied by the association owner. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Associations > Association owners and tenants - `View` `Edit` Associations > Ownership Accounts - `View`")
    async def update_association_owner_occupancy_status(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        owner_id: Annotated[int, Field(description="ownerId")],
        unit_id: Annotated[int, Field(description="unitId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/associations/owners/{ownerId}/units/{unitId}", path_params={"ownerId": owner_id, "unitId": unit_id}, query={}, body=body)

    @mcp.tool(name="get_association_ownership_account_notes", description="[Ownership Accounts] Retrieve all notes. Retrieves notes for an ownership account. Required permission(s): Associations > OwnershipAccounts - `View`")
    async def get_association_ownership_account_notes(
        ownership_account_id: Annotated[int, Field(description="ownershipAccountId")],
        updateddatetimefrom: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        updateddatetimeto: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        lastupdatedbyuserid: Annotated[int | None, Field(description="Filters results to only notes that were last updated by the specified user identifier.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/ownershipaccounts/{ownershipAccountId}/notes", path_params={"ownershipAccountId": ownership_account_id}, query={"updateddatetimefrom": updateddatetimefrom, "updateddatetimeto": updateddatetimeto, "lastupdatedbyuserid": lastupdatedbyuserid, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_association_ownership_account_note", description="[Ownership Accounts] Create a note. Creates a new ownership account note. Required permission(s): Associations > Ownership accounts - `View` `Edit`")
    async def create_association_ownership_account_note(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        ownership_account_id: Annotated[int, Field(description="ownershipAccountId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/associations/ownershipaccounts/{ownershipAccountId}/notes", path_params={"ownershipAccountId": ownership_account_id}, query={}, body=body)

    @mcp.tool(name="get_association_ownership_account_note_by_note_id", description="[Ownership Accounts] Retrieve a note. Retrieves an ownership account note. Required permission(s): Associations > OwnershipAccounts - `View`")
    async def get_association_ownership_account_note_by_note_id(
        ownership_account_id: Annotated[int, Field(description="ownershipAccountId")],
        note_id: Annotated[int, Field(description="noteId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/ownershipaccounts/{ownershipAccountId}/notes/{noteId}", path_params={"ownershipAccountId": ownership_account_id, "noteId": note_id}, query={}, body=None)

    @mcp.tool(name="update_association_ownership_account_note", description="[Ownership Accounts] Update a note. Updates an association ownership account note. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Associations > Ownership Accounts - `View` `Edit`")
    async def update_association_ownership_account_note(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        ownership_account_id: Annotated[int, Field(description="ownershipAccountId")],
        note_id: Annotated[int, Field(description="noteId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/associations/ownershipaccounts/{ownershipAccountId}/notes/{noteId}", path_params={"ownershipAccountId": ownership_account_id, "noteId": note_id}, query={}, body=body)

    @mcp.tool(name="get_ownership_account_partial_payment_settings", description="[Ownership Accounts] Retrieve all partial payment settings for an ownership account. Retrieves partial payment settings for an ownership account. Required permission(s): Associations > OwnershipAccounts - `View`")
    async def get_ownership_account_partial_payment_settings(
        ownership_account_id: Annotated[int, Field(description="ownershipAccountId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/ownershipaccounts/{ownershipAccountId}/partialpaymentsettings", path_params={"ownershipAccountId": ownership_account_id}, query={}, body=None)

    @mcp.tool(name="update_patch_ownership_account_partial_payment", description="[Ownership Accounts] Update partial payment settings for an ownership account. Updates partial payment settings for an ownership account. Required Permission(s): Associations > Ownership Accounts - `View` `Edit` Administration > Application Settings - `View` `Edit`")
    async def update_patch_ownership_account_partial_payment(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        ownership_account_id: Annotated[int, Field(description="ownershipAccountId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PATCH", "/v1/associations/ownershipaccounts/{ownershipAccountId}/partialpaymentsettings", path_params={"ownershipAccountId": ownership_account_id}, query={}, body=body)

    @mcp.tool(name="create_ownership_accounts_charge_recurring_transaction", description="[Ownership Account Transactions] Create a recurring charge. Creates a recurring charge transaction that will post automatically on the specified ownership account ledger. Required permission(s): Associations > Ownership account transactions - `View` `Edit`")
    async def create_ownership_accounts_charge_recurring_transaction(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        ownership_account_id: Annotated[int, Field(description="ownershipAccountId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/associations/ownershipaccounts/{ownershipAccountId}/recurringcharges", path_params={"ownershipAccountId": ownership_account_id}, query={}, body=body)

    @mcp.tool(name="get_ownership_accounts_charge_recurring_transaction_by_id", description="[Ownership Account Transactions] Retrieve a recurring charge. Retrieves a recurring charge. Required permission(s): Associations > Ownership account transactions - `View`")
    async def get_ownership_accounts_charge_recurring_transaction_by_id(
        ownership_account_id: Annotated[int, Field(description="ownershipAccountId")],
        transaction_id: Annotated[int, Field(description="transactionId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/ownershipaccounts/{ownershipAccountId}/recurringcharges/{transactionId}", path_params={"ownershipAccountId": ownership_account_id, "transactionId": transaction_id}, query={}, body=None)

    @mcp.tool(name="create_ownership_account_credit_recurring_transaction", description="[Ownership Account Transactions] Create a recurring credit. Creates a recurring credit transaction that will post automatically on the specified ownership account ledger. Required permission(s): Associations > Ownership account transactions - `View` `Edit`")
    async def create_ownership_account_credit_recurring_transaction(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        ownership_account_id: Annotated[int, Field(description="ownershipAccountId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/associations/ownershipaccounts/{ownershipAccountId}/recurringcredits", path_params={"ownershipAccountId": ownership_account_id}, query={}, body=body)

    @mcp.tool(name="get_ownership_account_recurring_credit_by_id", description="[Ownership Account Transactions] Retrieve a recurring credit. Retrieves a recurring credit. Required permission(s): Associations > Ownership account transactions - `View`")
    async def get_ownership_account_recurring_credit_by_id(
        ownership_account_id: Annotated[int, Field(description="ownershipAccountId")],
        transaction_id: Annotated[int, Field(description="transactionId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/ownershipaccounts/{ownershipAccountId}/recurringcredits/{transactionId}", path_params={"ownershipAccountId": ownership_account_id, "transactionId": transaction_id}, query={}, body=None)

    @mcp.tool(name="create_ownership_account_recurring_payment", description="[Ownership Account Transactions] Create a recurring payment. Creates a recurring payment that will post automatically on the specified ownership account ledger. Required permission(s): Associations > Ownership account transactions - `View` `Edit`")
    async def create_ownership_account_recurring_payment(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        ownership_account_id: Annotated[int, Field(description="ownershipAccountId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/associations/ownershipaccounts/{ownershipAccountId}/recurringpayments", path_params={"ownershipAccountId": ownership_account_id}, query={}, body=body)

    @mcp.tool(name="get_recurring_ownership_account_payments_by_id", description="[Ownership Account Transactions] Retrieve a recurring payment. Retrieves a recurring payment. Required permission(s): Associations > Ownership account transactions - `View`")
    async def get_recurring_ownership_account_payments_by_id(
        ownership_account_id: Annotated[int, Field(description="ownershipAccountId")],
        payment_id: Annotated[int, Field(description="paymentId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/ownershipaccounts/{ownershipAccountId}/recurringpayments/{paymentId}", path_params={"ownershipAccountId": ownership_account_id, "paymentId": payment_id}, query={}, body=None)

    @mcp.tool(name="get_architectural_request_file_async", description="[Architectural Requests] Retrieve an architectural request file. Retrieves an architectural request file. Required permission(s): Associations > Associations and units - `View` Associations > Ownership accounts - `View` Associations > Association owners and tenants - `View` Associations > Architectural requests - `View`")
    async def get_architectural_request_file_async(
        architectural_request_id: Annotated[int, Field(description="architecturalRequestId")],
        file_id: Annotated[int, Field(description="fileId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/ownershipaccounts/architecturalrequests/{architecturalRequestId}/files/{fileId}", path_params={"architecturalRequestId": architectural_request_id, "fileId": file_id}, query={}, body=None)

    @mcp.tool(name="create_download_architectural_request_file_async", description="[Architectural Requests] Download an architectural request file. Downloads a specific file associated to the architectural request. Required permission(s): Associations > Associations and units - `View` Associations > Ownership accounts - `View` Associations > Association owners and tenants - `View` Associations > Architectural requests - `View`")
    async def create_download_architectural_request_file_async(
        architectural_request_id: Annotated[int, Field(description="architecturalRequestId")],
        file_id: Annotated[int, Field(description="fileId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/associations/ownershipaccounts/architecturalrequests/{architecturalRequestId}/files/{fileId}/downloadrequests", path_params={"architecturalRequestId": architectural_request_id, "fileId": file_id}, query={}, body=None)

    @mcp.tool(name="create_pre_authenticated_file_upload_request", description="[Architectural Requests] Upload an architectural request file. Uploads a file and associates it to the specified architectural request record. Uploading a file requires making two API requests. Each step is outlined below. Step 1 - Save file metadata The first step in the file upload process is to submit the file metadata to `/v1/associations/ownershipaccounts/architecturalrequests/{architecturalRequestId:int}/files/uploads`. The response of this call will contain an upload URL and a collection of headers that will be used in step 2 to generate the request for the file binary upload. NOTE: The response data will expire after 5 minutes. The file metadata will not be saved in the Buildium system if step 2 of this process is not completed successfully. Step 2 - Upload the file binary Uploading the file binary will require using the response from step 1 to form a PUT request to the Buildium file provider. Follow ...")
    async def create_pre_authenticated_file_upload_request(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        architectural_request_id: Annotated[int, Field(description="architecturalRequestId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/associations/ownershipaccounts/architecturalrequests/{architecturalRequestId}/files/uploads", path_params={"architecturalRequestId": architectural_request_id}, query={}, body=body)

    @mcp.tool(name="get_recurring_transactions_for_all_ownership_accounts", description="[Ownership Account Transactions] Retrieve all recurring transactions for all ownership accounts. Retrieves all recurring transactions for all ownership accounts. Required permission(s): Associations > Ownership account transactions - `View`")
    async def get_recurring_transactions_for_all_ownership_accounts(
        ownershipaccountids: Annotated[list[int] | None, Field(description="Filters results to only include records associated with the provided ownership account Ids.")] = None,
        createddatetimefrom: Annotated[str | None, Field(description="Filters results to recurring transactions created after the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. The maximum date range is 365 days.")] = None,
        createddatetimeto: Annotated[str | None, Field(description="Filters results to recurring transactions created before the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. The maximum date range is 365 days.")] = None,
        lastupdatedfrom: Annotated[str | None, Field(description="Filters results to recurring transactions last updated after the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. The maximum date range is 365 days.")] = None,
        lastupdatedto: Annotated[str | None, Field(description="Filters results to recurring transactions last updated before the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. The maximum date range is 365 days.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/ownershipaccounts/recurringtransactions", path_params={}, query={"ownershipaccountids": ownershipaccountids, "createddatetimefrom": createddatetimefrom, "createddatetimeto": createddatetimeto, "lastupdatedfrom": lastupdatedfrom, "lastupdatedto": lastupdatedto, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_association_tenant_notes", description="[Association Tenants] Retrieve all notes. Retrieves all association tenant notes. Required permission(s): Associations > Association owners and tenants - `View`")
    async def get_association_tenant_notes(
        tenant_id: Annotated[int, Field(description="tenantId")],
        updateddatetimefrom: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        updateddatetimeto: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        lastupdatedbyuserid: Annotated[int | None, Field(description="Filters results to only notes that were last updated by the specified user identifier.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/tenants/{tenantId}/notes", path_params={"tenantId": tenant_id}, query={"updateddatetimefrom": updateddatetimefrom, "updateddatetimeto": updateddatetimeto, "lastupdatedbyuserid": lastupdatedbyuserid, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_association_tenant_note", description="[Association Tenants] Create a note. Creates an association tenant note. Required permission(s): Associations > Association owners and tenants - `View` `Edit`")
    async def create_association_tenant_note(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        tenant_id: Annotated[int, Field(description="tenantId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/associations/tenants/{tenantId}/notes", path_params={"tenantId": tenant_id}, query={}, body=body)

    @mcp.tool(name="get_association_tenant_note_by_id", description="[Association Tenants] Retrieve a note. Retrieves an association tenant note. Required permission(s): Associations > Association owners and tenants - `View`")
    async def get_association_tenant_note_by_id(
        tenant_id: Annotated[int, Field(description="tenantId")],
        note_id: Annotated[int, Field(description="noteId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/tenants/{tenantId}/notes/{noteId}", path_params={"tenantId": tenant_id, "noteId": note_id}, query={}, body=None)

    @mcp.tool(name="update_association_tenant_note", description="[Association Tenants] Update a note. Updates an association tenant note. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Associations > Association owners and tenants - `View` `Edit`")
    async def update_association_tenant_note(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        tenant_id: Annotated[int, Field(description="tenantId")],
        note_id: Annotated[int, Field(description="noteId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/associations/tenants/{tenantId}/notes/{noteId}", path_params={"tenantId": tenant_id, "noteId": note_id}, query={}, body=body)

    @mcp.tool(name="get_association_unit_notes", description="[Association Units] Retrieve all notes. Retrieves all association unit notes. Required permission(s): Associations > Associations and units - `View`")
    async def get_association_unit_notes(
        unit_id: Annotated[int, Field(description="unitId")],
        updateddatetimefrom: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        updateddatetimeto: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        lastupdatedbyuserid: Annotated[int | None, Field(description="Filters results to only notes that were last updated by the specified user identifier.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/units/{unitId}/notes", path_params={"unitId": unit_id}, query={"updateddatetimefrom": updateddatetimefrom, "updateddatetimeto": updateddatetimeto, "lastupdatedbyuserid": lastupdatedbyuserid, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_association_unit_note", description="[Association Units] Create a note. Creates a new association unit note. Required permission(s): Associations > Associations and units - `View` `Edit`")
    async def create_association_unit_note(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        unit_id: Annotated[int, Field(description="unitId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/associations/units/{unitId}/notes", path_params={"unitId": unit_id}, query={}, body=body)

    @mcp.tool(name="get_association_unit_note_by_note_id", description="[Association Units] Retrieve a note. Retrieves an association unit note. Required permission(s): Associations > Associations and units - `View`")
    async def get_association_unit_note_by_note_id(
        unit_id: Annotated[int, Field(description="unitId")],
        note_id: Annotated[int, Field(description="noteId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/associations/units/{unitId}/notes/{noteId}", path_params={"unitId": unit_id, "noteId": note_id}, query={}, body=None)

    @mcp.tool(name="update_association_unit_note", description="[Association Units] Update a note. Updates an association unit note. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Associations > Associations and units - `View` `Edit`")
    async def update_association_unit_note(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        unit_id: Annotated[int, Field(description="unitId")],
        note_id: Annotated[int, Field(description="noteId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/associations/units/{unitId}/notes/{noteId}", path_params={"unitId": unit_id, "noteId": note_id}, query={}, body=body)

    @mcp.tool(name="get_bank_account_checks", description="[Bank Accounts] Retrieve all checks. Retrieves all bank account checks. Required permission(s): Accounting > Bank Accounts - `View` Accounting > General Ledger Transactions - `View` (Required for checks associated with a Company)")
    async def get_bank_account_checks(
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        startdate: Annotated[str, Field(description="Filters results to any transactions that were recorded on or after the specified date. The value must be formatted as YYYY-MM-DD.")],
        enddate: Annotated[str, Field(description="Filters results to any transactions that were recorded on or before the specified date. The value must be formatted as YYYY-MM-DD.")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/bankaccounts/{bankAccountId}/checks", path_params={"bankAccountId": bank_account_id}, query={"startdate": startdate, "enddate": enddate, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_bank_account_check", description="[Bank Accounts] Create a check. Creates a check. Required permission(s): Accounting > Bank Accounts - `View` `Edit`")
    async def create_bank_account_check(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/bankaccounts/{bankAccountId}/checks", path_params={"bankAccountId": bank_account_id}, query={}, body=body)

    @mcp.tool(name="get_check_for_bank_account", description="[Bank Accounts] Retrieve a check. Retrieves a bank account check. Required permission(s): Accounting > Bank Accounts - `View` Accounting > General Ledger Transactions - `View` (Required for checks associated with a Company)")
    async def get_check_for_bank_account(
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        check_id: Annotated[int, Field(description="checkId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/bankaccounts/{bankAccountId}/checks/{checkId}", path_params={"bankAccountId": bank_account_id, "checkId": check_id}, query={}, body=None)

    @mcp.tool(name="update_check_for_bank_account", description="[Bank Accounts] Update a check. Updates a check. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Accounting > Bank Accounts - `View` `Edit`")
    async def update_check_for_bank_account(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        check_id: Annotated[int, Field(description="checkId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/bankaccounts/{bankAccountId}/checks/{checkId}", path_params={"bankAccountId": bank_account_id, "checkId": check_id}, query={}, body=body)

    @mcp.tool(name="get_files_for_bank_account_check", description="[Bank Accounts] Retrieve all files for a check. Retrieves the metadata for all files associated to the specified check. Required permission(s): Accounting > Bank Accounts - `View` Accounting > General Ledger Transactions - `View` (Required for checks associated with a Company)")
    async def get_files_for_bank_account_check(
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        check_id: Annotated[int, Field(description="checkId")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/bankaccounts/{bankAccountId}/checks/{checkId}/files", path_params={"bankAccountId": bank_account_id, "checkId": check_id}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_bank_account_check_file_by_id", description="[Bank Accounts] Retrieve a file for a check. Retrieves the metadata for a specific file associated with the specified check. Required permission(s): Accounting > Bank Accounts - `View` Accounting > General Ledger Transactions - `View` (Required for checks associated with a Company)")
    async def get_bank_account_check_file_by_id(
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        check_id: Annotated[int, Field(description="checkId")],
        file_id: Annotated[int, Field(description="fileId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/bankaccounts/{bankAccountId}/checks/{checkId}/files/{fileId}", path_params={"bankAccountId": bank_account_id, "checkId": check_id, "fileId": file_id}, query={}, body=None)

    @mcp.tool(name="delete_bank_account_check_file", description="[Bank Accounts] Delete a file for a check. Deletes a file for a check Required permission(s): Accounting > BankAccounts - `View` `Edit` `Delete` Accounting > General Ledger Transactions - `View` (Required for checks associated with a Company)")
    async def delete_bank_account_check_file(
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        check_id: Annotated[int, Field(description="checkId")],
        file_id: Annotated[int, Field(description="fileId")],
    ) -> dict[str, Any]:
        return await client.raw_request("DELETE", "/v1/bankaccounts/{bankAccountId}/checks/{checkId}/files/{fileId}", path_params={"bankAccountId": bank_account_id, "checkId": check_id, "fileId": file_id}, query={}, body=None)

    @mcp.tool(name="create_download_check_file", description="[Bank Accounts] Download a file for a check. Downloads a specific file associated to the check. Required permission(s): Accounting > Bank Accounts - `View` Accounting > General Ledger Transactions - `View` (Required for checks associated with a Company)")
    async def create_download_check_file(
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        check_id: Annotated[int, Field(description="checkId")],
        file_id: Annotated[int, Field(description="fileId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/bankaccounts/{bankAccountId}/checks/{checkId}/files/{fileId}/downloadrequests", path_params={"bankAccountId": bank_account_id, "checkId": check_id, "fileId": file_id}, query={}, body=None)

    @mcp.tool(name="create_upload_request_v2", description="[Bank Accounts] Upload a file for a check. Uploads a file and associates it to the specified check record. Uploading a file requires making two API requests. Each step is outlined below. Step 1 - Save file metadata The first step in the file upload process is to submit the file metadata to `/v1/bankaccounts/{bankAccountId}/checks/{checkId}/files/uploads`. The response of this call will contain an upload URL and a collection of headers that will be used in step 2 to generate the request for the file binary upload. NOTE: The response data will expire after 5 minutes. The file metadata will not be saved in the Buildium system if step 2 of this process is not completed successfully. Step 2 - Upload the file binary Uploading the file binary will require using the response from step 1 to form a PUT request to the Buildium file provider. Follow these steps to create the request: 1. Form a PUT request using ...")
    async def create_upload_request_v2(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        check_id: Annotated[int, Field(description="checkId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/bankaccounts/{bankAccountId}/checks/{checkId}/files/uploads", path_params={"bankAccountId": bank_account_id, "checkId": check_id}, query={}, body=body)

    @mcp.tool(name="get_bank_account_deposits", description="[Bank Accounts] Retrieve all deposits. Retrieves all bank account deposits. Required permission(s): Accounting > BankAccount - `View` Accounting > General Ledger Transactions - `View` (Required for deposits associated with a Company)")
    async def get_bank_account_deposits(
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        startdate: Annotated[str, Field(description="Filters results to any deposits that were recorded on or after the specified date. The value must be formatted as YYYY-MM-DD.")],
        enddate: Annotated[str, Field(description="Filters results to any deposits that were recorded on or before the specified date. The value must be formatted as YYYY-MM-DD.")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/bankaccounts/{bankAccountId}/deposits", path_params={"bankAccountId": bank_account_id}, query={"startdate": startdate, "enddate": enddate, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_bank_account_deposit", description="[Bank Accounts] Create a deposit. Creates a deposit. Required permission(s): Accounting > Bank Accounts - `View` `Edit`")
    async def create_bank_account_deposit(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/bankaccounts/{bankAccountId}/deposits", path_params={"bankAccountId": bank_account_id}, query={}, body=body)

    @mcp.tool(name="get_bank_account_deposit_by_id", description="[Bank Accounts] Retrieve a deposit. Retrieves a bank account deposit. Required permission(s): Accounting > BankAccount - `View` Accounting > General Ledger Transactions - `View` (Required for deposits associated with a Company)")
    async def get_bank_account_deposit_by_id(
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        deposit_id: Annotated[int, Field(description="depositId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/bankaccounts/{bankAccountId}/deposits/{depositId}", path_params={"bankAccountId": bank_account_id, "depositId": deposit_id}, query={}, body=None)

    @mcp.tool(name="update_bank_account_deposit", description="[Bank Accounts] Update a deposit. Updates a deposit. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Accounting > Bank Accounts - `View` `Edit`")
    async def update_bank_account_deposit(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        deposit_id: Annotated[int, Field(description="depositId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/bankaccounts/{bankAccountId}/deposits/{depositId}", path_params={"bankAccountId": bank_account_id, "depositId": deposit_id}, query={}, body=body)

    @mcp.tool(name="get_all_quick_deposits", description="[Bank Accounts] Retrieve all quick deposits. Retrieves all quick deposits. Required permission(s): Accounting > BankAccount - `View`")
    async def get_all_quick_deposits(
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        startdate: Annotated[str, Field(description="Filters results to any transactions that were recorded on or after the specified date. The value must be formatted as YYYY-MM-DD.")],
        enddate: Annotated[str, Field(description="Filters results to any transactions that were recorded on or before the specified date. The value must be formatted as YYYY-MM-DD.")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/bankaccounts/{bankAccountId}/quickdeposits", path_params={"bankAccountId": bank_account_id}, query={"startdate": startdate, "enddate": enddate, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_quick_deposit", description="[Bank Accounts] Create a quick deposit. Creates a quick deposit. Required permission(s): Accounting > BankAccount - `View` `Edit`")
    async def create_quick_deposit(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/bankaccounts/{bankAccountId}/quickdeposits", path_params={"bankAccountId": bank_account_id}, query={}, body=body)

    @mcp.tool(name="get_quick_deposit_by_id", description="[Bank Accounts] Retrieve a quick deposit. Retrieves a quick deposit. Required permission(s): Accounting > BankAccount - `View`")
    async def get_quick_deposit_by_id(
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        quick_deposit_id: Annotated[int, Field(description="quickDepositId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/bankaccounts/{bankAccountId}/quickdeposits/{quickDepositId}", path_params={"bankAccountId": bank_account_id, "quickDepositId": quick_deposit_id}, query={}, body=None)

    @mcp.tool(name="update_quick_deposit", description="[Bank Accounts] Update a quick deposit. Updates a quick deposit. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Accounting > Bank Accounts - `View` `Edit`")
    async def update_quick_deposit(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        quick_deposit_id: Annotated[int, Field(description="quickDepositId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/bankaccounts/{bankAccountId}/quickdeposits/{quickDepositId}", path_params={"bankAccountId": bank_account_id, "quickDepositId": quick_deposit_id}, query={}, body=body)

    @mcp.tool(name="get_reconciliations", description="[Bank Accounts] Retrieve all reconciliations. Retrieves all bank account reconciliations. Reconciliations can only be retrieved for bank accounts that are not linked externally. Required permission(s): Accounting > BankAccount - `View`")
    async def get_reconciliations(
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/bankaccounts/{bankAccountId}/reconciliations", path_params={"bankAccountId": bank_account_id}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_pending_reconciliations", description="[Bank Accounts] Create a reconciliation. Creates a reconciliation. Reconciliations can only be created for bank accounts that are not linked externally. Required permission(s): Accounting > BankAccount - `View` `Edit`")
    async def create_pending_reconciliations(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/bankaccounts/{bankAccountId}/reconciliations", path_params={"bankAccountId": bank_account_id}, query={}, body=body)

    @mcp.tool(name="get_reconciliation_by_id", description="[Bank Accounts] Retrieve a reconciliation. Retrieves a bank account reconciliation. Reconciliations can only be retrieved for bank accounts that are not linked externally. Required permission(s): Accounting > BankAccount - `View`")
    async def get_reconciliation_by_id(
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        reconciliation_id: Annotated[int, Field(description="reconciliationId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/bankaccounts/{bankAccountId}/reconciliations/{reconciliationId}", path_params={"bankAccountId": bank_account_id, "reconciliationId": reconciliation_id}, query={}, body=None)

    @mcp.tool(name="update_reconciliation", description="[Bank Accounts] Update a reconciliation. Updates a reconciliation. Reconciliations can only be updated for bank accounts that are not linked externally. Required permission(s): Accounting > BankAccount - `View` `Edit`")
    async def update_reconciliation(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        reconciliation_id: Annotated[int, Field(description="reconciliationId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/bankaccounts/{bankAccountId}/reconciliations/{reconciliationId}", path_params={"bankAccountId": bank_account_id, "reconciliationId": reconciliation_id}, query={}, body=body)

    @mcp.tool(name="get_reconciliation_balance_by_id", description="[Bank Accounts] Retrieve a reconciliation's balance. Retrieves a bank account reconciliation's balance. Reconciliation balances can only be retrieved for bank accounts that are not linked externally. Required permission(s): Accounting > BankAccount - `View`")
    async def get_reconciliation_balance_by_id(
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        reconciliation_id: Annotated[int, Field(description="reconciliationId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/bankaccounts/{bankAccountId}/reconciliations/{reconciliationId}/balances", path_params={"bankAccountId": bank_account_id, "reconciliationId": reconciliation_id}, query={}, body=None)

    @mcp.tool(name="update_reconciliation_balances", description="[Bank Accounts] Update a reconciliation's balance. Updates a bank account reconciliation's balance. Reconciliation balances can only be updated for bank accounts that are not linked externally. Required permission(s): Accounting > BankAccount - `View` `Edit`")
    async def update_reconciliation_balances(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        reconciliation_id: Annotated[int, Field(description="reconciliationId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/bankaccounts/{bankAccountId}/reconciliations/{reconciliationId}/balances", path_params={"bankAccountId": bank_account_id, "reconciliationId": reconciliation_id}, query={}, body=body)

    @mcp.tool(name="create_clear_transactions", description="[Bank Accounts] Clear transactions for a reconciliation. Clears transactions for a reconciliation. Reconciliation transactions can only be cleared for bank accounts that are not linked externally. Required permission(s): Accounting > BankAccount - `View` `Edit`")
    async def create_clear_transactions(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        reconciliation_id: Annotated[int, Field(description="reconciliationId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/bankaccounts/{bankAccountId}/reconciliations/{reconciliationId}/cleartransactionsrequest", path_params={"bankAccountId": bank_account_id, "reconciliationId": reconciliation_id}, query={}, body=body)

    @mcp.tool(name="create_finalize_reconciliation", description="[Bank Accounts] Finalize a manual reconciliation. Finalizes a manual reconciliation. Reconciliations can only be finalized for bank accounts that are not linked externally. Required permission(s): Accounting > BankAccount - `View` `Edit`")
    async def create_finalize_reconciliation(
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        reconciliation_id: Annotated[int, Field(description="reconciliationId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/bankaccounts/{bankAccountId}/reconciliations/{reconciliationId}/finalizerequest", path_params={"bankAccountId": bank_account_id, "reconciliationId": reconciliation_id}, query={}, body=None)

    @mcp.tool(name="get_bank_account_reconciliation_transactions", description="[Bank Accounts] Retrieve all transactions for a reconciliation. Retrieves all transactions, both cleared and uncleared, up to the Statement Ending Date of the related reconciliation. This is true for pending and completed reconciliations. Transactions can only be retrieved for bank accounts that are not linked externally. Required permission(s): Accounting > BankAccount - `View`")
    async def get_bank_account_reconciliation_transactions(
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        reconciliation_id: Annotated[int, Field(description="reconciliationId")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/bankaccounts/{bankAccountId}/reconciliations/{reconciliationId}/transactions", path_params={"bankAccountId": bank_account_id, "reconciliationId": reconciliation_id}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_unclear_transactions", description="[Bank Accounts] Un-clear transactions for a reconciliation. Un-clears transactions for a reconciliation. Reconciliation transactions can only be un-cleared for bank accounts that are not linked externally. Required permission(s): Accounting > BankAccount - `View` `Edit`")
    async def create_unclear_transactions(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        reconciliation_id: Annotated[int, Field(description="reconciliationId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/bankaccounts/{bankAccountId}/reconciliations/{reconciliationId}/uncleartransactionsrequest", path_params={"bankAccountId": bank_account_id, "reconciliationId": reconciliation_id}, query={}, body=body)

    @mcp.tool(name="get_bank_account_transactions", description="[Bank Accounts] Retrieve all transactions. Retrieves all bank account transactions. Note: When using the `orderby` query string parameter, the only supported parameter is `EntryDate`. Required permission(s): Accounting > Bank Accounts - `View`")
    async def get_bank_account_transactions(
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        startdate: Annotated[str, Field(description="Filters results to any transactions that were recorded on or after the specified date. The value must be formatted as YYYY-MM-DD.")],
        enddate: Annotated[str, Field(description="Filters results to any transactions that were recorded on or before the specified date. The value must be formatted as YYYY-MM-DD.")],
        selectionentityid: Annotated[int | None, Field(description="Filters results to any transaction containing journal lines for an entity associated with the specified entity id value. The id must be of the type specified in SelectionEntityType.")] = None,
        selectionentitytype: Annotated[str | None, Field(description="Specifies the type of entity that SelectionEntityId refers to.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/bankaccounts/{bankAccountId}/transactions", path_params={"bankAccountId": bank_account_id}, query={"selectionentityid": selectionentityid, "selectionentitytype": selectionentitytype, "startdate": startdate, "enddate": enddate, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_bank_account_transfers", description="[Bank Accounts] Retrieve all transfers. Retrieves all bank account transfers. Required permission(s): Accounting > BankAccount - `View`")
    async def get_bank_account_transfers(
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        startdate: Annotated[str, Field(description="Filters results to any transfers that were recorded on or after the specified date. The value must be formatted as YYYY-MM-DD.")],
        enddate: Annotated[str, Field(description="Filters results to any transfers that were recorded on or before the specified date. The value must be formatted as YYYY-MM-DD.")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/bankaccounts/{bankAccountId}/transfers", path_params={"bankAccountId": bank_account_id}, query={"startdate": startdate, "enddate": enddate, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_bank_account_transfer", description="[Bank Accounts] Create a transfer. Creates a bank account transfer. Required permission(s): Accounting > Bank Accounts - `View` `Edit`")
    async def create_bank_account_transfer(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/bankaccounts/{bankAccountId}/transfers", path_params={"bankAccountId": bank_account_id}, query={}, body=body)

    @mcp.tool(name="get_bank_account_transfer_by_id", description="[Bank Accounts] Retrieve a transfer. Retrieves a bank account transfer. Required permission(s): Accounting > Bank Accounts - `View`")
    async def get_bank_account_transfer_by_id(
        bank_account_id: Annotated[int, Field(description="The bank account identifier.")],
        transfer_id: Annotated[int, Field(description="The transfer identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/bankaccounts/{bankAccountId}/transfers/{transferId}", path_params={"bankAccountId": bank_account_id, "transferId": transfer_id}, query={}, body=None)

    @mcp.tool(name="update_bank_account_transfer", description="[Bank Accounts] Update a transfer. Updates a bank account transfer. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Accounting > Bank Accounts - `View` `Edit`")
    async def update_bank_account_transfer(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        transfer_id: Annotated[int, Field(description="transferId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/bankaccounts/{bankAccountId}/transfers/{transferId}", path_params={"bankAccountId": bank_account_id, "transferId": transfer_id}, query={}, body=body)

    @mcp.tool(name="get_undeposited_funds", description="[Bank Accounts] Retrieve all undeposited funds. Retrieve all bank account undeposited funds. Required permission(s): Accounting > Bank Accounts - `View`")
    async def get_undeposited_funds(
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/bankaccounts/{bankAccountId}/undepositedfunds", path_params={"bankAccountId": bank_account_id}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_bank_account_withdrawals", description="[Bank Accounts] Retrieve all withdrawals. Retrieves all bank account withdrawals. Required permission(s): Accounting > BankAccounts - `View`")
    async def get_bank_account_withdrawals(
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        startdate: Annotated[str, Field(description="Filters results to any transactions that were recorded on or after the specified date. The value must be formatted as YYYY-MM-DD.")],
        enddate: Annotated[str, Field(description="Filters results to any transactions that were recorded on or before the specified date. The value must be formatted as YYYY-MM-DD.")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/bankaccounts/{bankAccountId}/withdrawals", path_params={"bankAccountId": bank_account_id}, query={"startdate": startdate, "enddate": enddate, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_withdrawal_for_bank_account", description="[Bank Accounts] Create a withdrawal. Creates a bank account withdrawal. Required permission(s): Accounting > Bank Accounts - `View` `Edit`")
    async def create_withdrawal_for_bank_account(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/bankaccounts/{bankAccountId}/withdrawals", path_params={"bankAccountId": bank_account_id}, query={}, body=body)

    @mcp.tool(name="get_bank_account_withdrawal_by_id", description="[Bank Accounts] Retrieve a withdrawal. Retrieves a bank account withdrawal. Required permission(s): Accounting > BankAccounts - `View`")
    async def get_bank_account_withdrawal_by_id(
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        withdrawal_id: Annotated[int, Field(description="withdrawalId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/bankaccounts/{bankAccountId}/withdrawals/{withdrawalId}", path_params={"bankAccountId": bank_account_id, "withdrawalId": withdrawal_id}, query={}, body=None)

    @mcp.tool(name="update_bank_account_withdrawal", description="[Bank Accounts] Update a withdrawal. Updates a bank account withdrawal. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Accounting > Bank Accounts - `View` `Edit`")
    async def update_bank_account_withdrawal(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        bank_account_id: Annotated[int, Field(description="bankAccountId")],
        withdrawal_id: Annotated[int, Field(description="withdrawalId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/bankaccounts/{bankAccountId}/withdrawals/{withdrawalId}", path_params={"bankAccountId": bank_account_id, "withdrawalId": withdrawal_id}, query={}, body=body)

    @mcp.tool(name="update_patch_bill", description="[Bills] Update a bill. Updates a bill. Required permission(s): Accounting > Bills - `View` `Edit`")
    async def update_patch_bill(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        bill_id: Annotated[int, Field(description="billId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PATCH", "/v1/bills/{billId}", path_params={"billId": bill_id}, query={}, body=body)

    @mcp.tool(name="get_all_files_for_bill", description="[Bills] Retrieve all files for a bill. Retrieves the metadata for all files associated to the specified bill. To download the actual file view the [Download a bill file](#tag/Bills/operation/ExternalApiBillFileDownloadRequests_DownloadBillFile). Required permission(s): Accounting > Bills - `View`")
    async def get_all_files_for_bill(
        bill_id: Annotated[int, Field(description="billId")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/bills/{billId}/files", path_params={"billId": bill_id}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_bill_file_by_id", description="[Bills] Retrieve a file for a bill. Retrieves the metadata for a specific file associated with the specified bill. Required permission(s): Accounting > Bills - `View`")
    async def get_bill_file_by_id(
        bill_id: Annotated[int, Field(description="billId")],
        file_id: Annotated[int, Field(description="fileId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/bills/{billId}/files/{fileId}", path_params={"billId": bill_id, "fileId": file_id}, query={}, body=None)

    @mcp.tool(name="delete_bill_file", description="[Bills] Delete a bill file. Deletes the specified file from a bill. The file will be permanently deleted from the Buildium platform and can not be recovered. Required permission(s): Accounting > Bills - `View` `Edit` `Delete`")
    async def delete_bill_file(
        bill_id: Annotated[int, Field(description="billId")],
        file_id: Annotated[int, Field(description="fileId")],
    ) -> dict[str, Any]:
        return await client.raw_request("DELETE", "/v1/bills/{billId}/files/{fileId}", path_params={"billId": bill_id, "fileId": file_id}, query={}, body=None)

    @mcp.tool(name="create_download_bill_file", description="[Bills] Download a bill file. Downloads a specific file associated to the bill. Required permission(s): Accounting > Bills - `View`")
    async def create_download_bill_file(
        bill_id: Annotated[int, Field(description="billId")],
        file_id: Annotated[int, Field(description="fileId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/bills/{billId}/files/{fileId}/downloadrequest", path_params={"billId": bill_id, "fileId": file_id}, query={}, body=None)

    @mcp.tool(name="create_upload_request", description="[Bills] Upload a bill file. Uploads a file and associates it to the specified bill record. Uploading a file requires making two API requests. Each step is outlined below. Step 1 - Save file metadata The first step in the file upload process is to submit the file metadata to `/v1/bills/{billId}/files/uploads`. The response of this call will contain an upload URL and a collection of headers that will be used in step 2 to generate the request for the file binary upload. NOTE: The response data will expire after 5 minutes. The file metadata will not be saved in the Buildium system if step 2 of this process is not completed successfully. Step 2 - Upload the file binary Uploading the file binary will require using the response from step 1 to form a PUT request to the Buildium file provider. Follow these steps to create the request: 1. Form a PUT request using the value of the `UploadUrl` property a...")
    async def create_upload_request(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        bill_id: Annotated[int, Field(description="billId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/bills/{billId}/files/uploads", path_params={"billId": bill_id}, query={}, body=body)

    @mcp.tool(name="create_multiple_bill_payments", description="[Bills] Create a payment for multiple bills with one check. Creates a payment for multiple bills with one check. Required permission(s): Accounting > Bills - `View` `Edit` Accounting > Bank Accounts - `View` `Edit`")
    async def create_multiple_bill_payments(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/bills/payments", path_params={}, query={}, body=body)

    @mcp.tool(name="get_budgets", description="[Budgets] Retrieve all budgets. Retrieves all budgets. Required permission(s): Accounting > Budgets - `View`")
    async def get_budgets(
        propertyids: Annotated[list[int] | None, Field(description="Filters results to any budget associated to any of the specified set of property ids.")] = None,
        fiscalyear: Annotated[int | None, Field(description="Filters results to any budgets that end in the given fiscal year. FiscalYear must be a positive number.")] = None,
        name: Annotated[str | None, Field(description="Filters results to any budgets whose name *contains* the specified value.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/budgets", path_params={}, query={"propertyids": propertyids, "fiscalyear": fiscalyear, "name": name, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_budget_async", description="[Budgets] Create a budget. Creates a budget. Required permission(s): Accounting > Budgets - `View` `Edit`")
    async def create_budget_async(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/budgets", path_params={}, query={}, body=body)

    @mcp.tool(name="get_budget_by_id", description="[Budgets] Retrieve a budget. Retrieves a budget. Required permission(s): Accounting > Budgets - `View`")
    async def get_budget_by_id(
        budget_id: Annotated[int, Field(description="budgetId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/budgets/{budgetId}", path_params={"budgetId": budget_id}, query={}, body=None)

    @mcp.tool(name="update_budget", description="[Budgets] Update a budget. Updates a budget. Required permission(s): Accounting > Budgets - `View` `Edit`")
    async def update_budget(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        budget_id: Annotated[int, Field(description="budgetId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/budgets/{budgetId}", path_params={"budgetId": budget_id}, query={}, body=body)

    @mcp.tool(name="get_client_leads", description="[Client Leads] Retrieve all client leads. Retrieves all client leads Note: When using the `orderby` query string parameter, the only supported options are DateReceived. Required permission(s): Administration > All Property Management - `View`")
    async def get_client_leads(
        leadstatuses: Annotated[list[str] | None, Field(description="Filters results to any client leads that are in one of the given statuses.")] = None,
        propertytypes: Annotated[list[str] | None, Field(description="Filters results to any client leads that have a property in one of the given property types.")] = None,
        datereceivedfrom: Annotated[str | None, Field(description="Filters results to any client leads that were received on or after the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        datereceivedto: Annotated[str | None, Field(description="Filters results to any client leads that were received on or before the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        includecreditedleads: Annotated[bool | None, Field(description="This will also return client leads that were credited. By default credited leads will not be returned.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/clientleads", path_params={}, query={"leadstatuses": leadstatuses, "propertytypes": propertytypes, "datereceivedfrom": datereceivedfrom, "datereceivedto": datereceivedto, "includecreditedleads": includecreditedleads, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_prospective_client", description="[Client Leads] Retrieve a client lead. Retrieves a specific client lead Required permission(s): Administration > All Property Management - `View`")
    async def get_prospective_client(
        client_lead_id: Annotated[int, Field(description="clientLeadId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/clientleads/{clientLeadId}", path_params={"clientLeadId": client_lead_id}, query={}, body=None)

    @mcp.tool(name="get_all_announcements", description="[Communications] Retrieve all announcements. Retrieves all announcements. Required permission(s): Communications > Announcements - `View`")
    async def get_all_announcements(
        announcementdatefrom: Annotated[str | None, Field(description="Filters results to any announcements created on or after the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        announcementdateto: Annotated[str | None, Field(description="Filters results to any announcements created on or before the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        entityid: Annotated[int | None, Field(description="Filters results to any announcement associated with the specified entity id value. The value must be of the type specified in the `EntityType` field.")] = None,
        entitytype: Annotated[str | None, Field(description="Specifies the type of entity that the `EntityId` field refers to. This field is required if the `EntityId` field is provided.")] = None,
        senderid: Annotated[int | None, Field(description="Unique identifier of the user that published the announcement.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/communications/announcements", path_params={}, query={"announcementdatefrom": announcementdatefrom, "announcementdateto": announcementdateto, "entityid": entityid, "entitytype": entitytype, "senderid": senderid, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_announcement", description="[Communications] Create an announcement. Creates and publishes an announcement. Required permission(s): Communications > Announcements - `View` `Edit`")
    async def create_announcement(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/communications/announcements", path_params={}, query={}, body=body)

    @mcp.tool(name="get_announcement_by_id", description="[Communications] Retrieve an announcement. Retrieves an announcement. Required permission(s): Communications > Announcements - `View`")
    async def get_announcement_by_id(
        announcement_id: Annotated[int, Field(description="announcementId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/communications/announcements/{announcementId}", path_params={"announcementId": announcement_id}, query={}, body=None)

    @mcp.tool(name="create_expire_announcement", description="[Communications] Expire an announcement. Removes the announcement from the Resident Center immediately. Required permission(s): Communications > Announcements - `View` `Edit`")
    async def create_expire_announcement(
        announcement_id: Annotated[int, Field(description="announcementId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/communications/announcements/{announcementId}/expirationrequest", path_params={"announcementId": announcement_id}, query={}, body=None)

    @mcp.tool(name="get_announcement_properties", description="[Communications] Retrieve all announcement properties. Retrieves a list of association and/or rental properties whose residents received the announcement. An empty response collection indicates that the announcement was sent to all properties at the time of its creation. Required permission(s): Communications > Announcements - `View`")
    async def get_announcement_properties(
        announcement_id: Annotated[int, Field(description="announcementId")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/communications/announcements/{announcementId}/properties", path_params={"announcementId": announcement_id}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_emails", description="[Communications] Retrieve all emails. Retrieves all emails. System generated emails are not included. Required permission(s): Communication > Emails - `View`")
    async def get_emails(
        sentdatetimefrom: Annotated[str, Field(description="Filters results to any emails whose sent date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ. The maximum date range is 90 days.")],
        sentdatetimeto: Annotated[str, Field(description="Filters results to any emails whose sent date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ. The maximum date range is 90 days.")],
        subject: Annotated[str | None, Field(description="Filters results to any email whose subject *contains* the specified value.")] = None,
        recipientnameoremail: Annotated[str | None, Field(description="Filters results to any email with a recipient whose name or email address *contains* the specified value.")] = None,
        senderuserid: Annotated[int | None, Field(description="Filters results to only emails that were sent by the specified user identifier.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/communications/emails", path_params={}, query={"sentdatetimefrom": sentdatetimefrom, "sentdatetimeto": sentdatetimeto, "subject": subject, "recipientnameoremail": recipientnameoremail, "senderuserid": senderuserid, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_email", description="[Communications] Send an email. Sends an email to one or more recipients using the specified email template. NOTE: Emails can only be sent to current tenants. Required permission(s): Communication > Emails - `View` `Edit`")
    async def create_email(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/communications/emails", path_params={}, query={}, body=body)

    @mcp.tool(name="get_email_by_id", description="[Communications] Retrieve an email. Retrieves the content of an email. System generated emails are not included. To retrieve the recipients of the email see the [Retrieve all email recipients](#tag/Communications/operation/ExternalApiEmailRecipients_GetEmailRecipients) endpoint. Required permission(s): Communications > Emails - `View`")
    async def get_email_by_id(
        email_id: Annotated[int, Field(description="emailId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/communications/emails/{emailId}", path_params={"emailId": email_id}, query={}, body=None)

    @mcp.tool(name="get_email_recipients", description="[Communications] Retrieve all email recipients. Retrieves all email recipients. Required permission(s): Communications > Email - `View` Optional Permissions: The following permissions are optional, but results with a missing permission will be filtered out. Maintenance > Vendors - `View` In order to retrieve recipients that are Vendors, you must have this permission. Administration > Users - `View` In order to see recipients that are Staff, you must have this permission.")
    async def get_email_recipients(
        email_id: Annotated[int, Field(description="emailId")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/communications/emails/{emailId}/recipients", path_params={"emailId": email_id}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_phone_logs", description="[Communications] Retrieve all phone logs. Retrieves all phone logs. Required permission(s): Communications > Timelines (Phone Logs) - `View`")
    async def get_phone_logs(
        fromdate: Annotated[str | None, Field(description="Filters results to any phone log whose call date is greater than or equal to the specified value.")] = None,
        todate: Annotated[str | None, Field(description="Filters results to any phone log whose call date is less than or equal to the specified value.")] = None,
        loggedbystaffuserids: Annotated[list[int] | None, Field(description="Filters results to any phone log that was logged by staff user(s).")] = None,
        subject: Annotated[str | None, Field(description="Filters results to any phone log whose subject *contains* the specified value.")] = None,
        participantentityid: Annotated[int | None, Field(description="Filters results to any phone logs that match the participant identifier. Note, if a value is provided in this field the `ParticipantEntityType` must also be provided.")] = None,
        participantentitytype: Annotated[str | None, Field(description="Filters results to any phone log with the specified participant type. This field is required if a value is provided for the `ParticipantEntityId` field.")] = None,
        unitagreementid: Annotated[int | None, Field(description="Filters results to any phone log with the specified unit agreement identifier. Note, if a value is provided in this field the `UnitAgreementType` must also be provided.")] = None,
        unitagreementtype: Annotated[str | None, Field(description="Filters results to any phone log with the specified unit agreement type. This field is required if a value is provided for the `UnitAgreementId` field.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/communications/phonelogs", path_params={}, query={"fromdate": fromdate, "todate": todate, "loggedbystaffuserids": loggedbystaffuserids, "subject": subject, "participantentityid": participantentityid, "participantentitytype": participantentitytype, "unitagreementid": unitagreementid, "unitagreementtype": unitagreementtype, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_phone_log", description="[Communications] Create a phone log. Creates a phone log. Required permission(s): Communications > Timelines (Phone Logs) - `View` `Edit`")
    async def create_phone_log(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/communications/phonelogs", path_params={}, query={}, body=body)

    @mcp.tool(name="get_phone_log_by_id", description="[Communications] Retrieve a phone log. Retrieves a specific phone log. Required permission(s): Communications > Timelines (Phone Logs) - `View`")
    async def get_phone_log_by_id(
        phone_log_id: Annotated[int, Field(description="The phone log identifier")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/communications/phonelogs/{phoneLogId}", path_params={"phoneLogId": phone_log_id}, query={}, body=None)

    @mcp.tool(name="update_phone_log", description="[Communications] Update a phone log. Update a phone log NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Communications > Timelines (Phone Logs) - `View` `Edit`")
    async def update_phone_log(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        phone_log_id: Annotated[int, Field(description="The phone log identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/communications/phonelogs/{phoneLogId}", path_params={"phoneLogId": phone_log_id}, query={}, body=body)

    @mcp.tool(name="get_mailing_templates", description="[Communications] Retrieve all communication templates. Retrieves all mailing and email templates. A template is a tool in Buildium that allows you to create \"mail merge\" templates for emails and postal mailings to easily send common messages to residents, rental owners and vendors. Required permission(s): Communications > Mailing Templates - `View` Optional Permissions: Rentals > Tenants - `View` Rentals > Property Rental owners - `View` Associations > Association owners and tenants - `View` Maintenance > Vendors - `View` Rentals > Applicants - `View`")
    async def get_mailing_templates(
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/communications/templates", path_params={}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_mailing_templates_by_id", description="[Communications] Retrieve a communication template. Retrieves a communication template. A template is a tool in Buildium that allows you to create \"mail merge\" templates for emails and postal mailings to easily send common messages to residents, rental owners and vendors. Required permission(s): Communications > Mailing Templates - `View` Optional Permissions: Rentals > Tenants - `View` Rentals > Property Rental owners - `View` Associations > Association owners and tenants - `View` Maintenance > Vendors - `View` Rentals > Applicants - `View`")
    async def get_mailing_templates_by_id(
        template_id: Annotated[int, Field(description="templateId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/communications/templates/{templateId}", path_params={"templateId": template_id}, query={}, body=None)

    @mcp.tool(name="get_credit_card_accounts", description="[Credit Card Accounts] Get all credit card accounts. Gets credit card accounts. Required permission(s): Accounting > Bank Accounts - `View`")
    async def get_credit_card_accounts(
        creditcardaccountstatus: Annotated[str | None, Field(description="Filters results by the status of the credit card account. If no status is specified, credit card accounts with any status will be returned.")] = None,
        name: Annotated[str | None, Field(description="Filters results to any credit card account whose name *contains* the specified value.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/creditcardaccounts", path_params={}, query={"creditcardaccountstatus": creditcardaccountstatus, "name": name}, body=None)

    @mcp.tool(name="create_credit_card_account", description="[Credit Card Accounts] Create a credit card account. Creates a credit card account. Required permission(s): Accounting > Banking - `View` `Edit`")
    async def create_credit_card_account(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/creditcardaccounts", path_params={}, query={}, body=body)

    @mcp.tool(name="get_credit_card_account", description="[Credit Card Accounts] Get a credit card account. Gets a credit card account. Required permission(s): Accounting > Bank Accounts - `View`")
    async def get_credit_card_account(
        credit_card_account_id: Annotated[int, Field(description="creditCardAccountId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/creditcardaccounts/{creditCardAccountId}", path_params={"creditCardAccountId": credit_card_account_id}, query={}, body=None)

    @mcp.tool(name="update_credit_card_account", description="[Credit Card Accounts] Update a credit card account. Updates a credit card account. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Accounting > Banking - `View` `Edit`")
    async def update_credit_card_account(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        credit_card_account_id: Annotated[int, Field(description="creditCardAccountId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/creditcardaccounts/{creditCardAccountId}", path_params={"creditCardAccountId": credit_card_account_id}, query={}, body=body)

    @mcp.tool(name="create_credit_card_account_balance_payment", description="[Credit Card Accounts] Create a credit card balance payment. Creates a credit card balance payment. Required permission(s): Accounting > Bank Accounts - `View` `Edit`")
    async def create_credit_card_account_balance_payment(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        credit_card_account_id: Annotated[int, Field(description="creditCardAccountId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/creditcardaccounts/{creditCardAccountId}/payments", path_params={"creditCardAccountId": credit_card_account_id}, query={}, body=body)

    @mcp.tool(name="get_credit_card_account_balance_payment_by_id", description="[Credit Card Accounts] Retrieve a credit card balance payment. Retrieves a credit card balance payment. Required permission(s): Accounting > BankAccount - `View`")
    async def get_credit_card_account_balance_payment_by_id(
        credit_card_account_id: Annotated[int, Field(description="creditCardAccountId")],
        journal_id: Annotated[int, Field(description="journalId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/creditcardaccounts/{creditCardAccountId}/payments/{journalId}", path_params={"creditCardAccountId": credit_card_account_id, "journalId": journal_id}, query={}, body=None)

    @mcp.tool(name="update_edit_credit_card_account_balance_payment", description="[Credit Card Accounts] Edit a credit card balance payment. Edits a credit card balance payment. Required permission(s): Accounting > Bank Accounts - `View` `Edit`")
    async def update_edit_credit_card_account_balance_payment(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        journal_id: Annotated[int, Field(description="journalId")],
        credit_card_account_id: Annotated[int, Field(description="creditCardAccountId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/creditcardaccounts/{creditCardAccountId}/payments/{journalId}", path_params={"journalId": journal_id, "creditCardAccountId": credit_card_account_id}, query={}, body=body)

    @mcp.tool(name="create_credit_card_account_account_purchase", description="[Credit Card Accounts] Create a credit card purchase. Creates a credit card purchase. Required permission(s): Accounting > Bank Accounts - `View` `Edit`")
    async def create_credit_card_account_account_purchase(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        credit_card_account_id: Annotated[int, Field(description="creditCardAccountId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/creditcardaccounts/{creditCardAccountId}/purchases", path_params={"creditCardAccountId": credit_card_account_id}, query={}, body=body)

    @mcp.tool(name="get_credit_card_account_purchase_by_id", description="[Credit Card Accounts] Retrieve a credit card purchase. Retrieves a credit card purchase. Required permission(s): Accounting > BankAccount - `View`")
    async def get_credit_card_account_purchase_by_id(
        credit_card_account_id: Annotated[int, Field(description="creditCardAccountId")],
        journal_id: Annotated[int, Field(description="journalId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/creditcardaccounts/{creditCardAccountId}/purchases/{journalId}", path_params={"creditCardAccountId": credit_card_account_id, "journalId": journal_id}, query={}, body=None)

    @mcp.tool(name="update_edit_credit_card_account_purchase", description="[Credit Card Accounts] Edit a credit card purchase. Edits a credit card purchase. Required permission(s): Accounting > Bank Accounts - `View` `Edit`")
    async def update_edit_credit_card_account_purchase(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        journal_id: Annotated[int, Field(description="journalId")],
        credit_card_account_id: Annotated[int, Field(description="creditCardAccountId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/creditcardaccounts/{creditCardAccountId}/purchases/{journalId}", path_params={"journalId": journal_id, "creditCardAccountId": credit_card_account_id}, query={}, body=body)

    @mcp.tool(name="get_credit_card_account_transactions", description="[Credit Card Accounts] Retrieve all transactions. Retrieves all credit card account transactions. Note: When using the `orderby` query string parameter, the only supported parameter is `EntryDate`. Required permission(s): Accounting > Bank Accounts - `View`")
    async def get_credit_card_account_transactions(
        credit_card_account_id: Annotated[int, Field(description="creditCardAccountId")],
        startdate: Annotated[str, Field(description="Filters results to any transactions that were recorded on or after the specified date. The value must be formatted as YYYY-MM-DD.")],
        enddate: Annotated[str, Field(description="Filters results to any transactions that were recorded on or before the specified date. The value must be formatted as YYYY-MM-DD.")],
        selectionentityid: Annotated[int | None, Field(description="Filters results to any transaction containing journal lines for an entity associated with the specified entity id value. The id must be of the type specified in SelectionEntityType.")] = None,
        selectionentitytype: Annotated[str | None, Field(description="Specifies the type of entity that SelectionEntityId refers to.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/creditcardaccounts/{creditCardAccountId}/transactions", path_params={"creditCardAccountId": credit_card_account_id}, query={"selectionentityid": selectionentityid, "selectionentitytype": selectionentitytype, "startdate": startdate, "enddate": enddate, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_credit_card_account_transaction_by_id", description="[Credit Card Accounts] Retrieve a transaction. Retrieves a specific credit card account transaction. Required permission(s): Accounting > Bank Accounts - `View`")
    async def get_credit_card_account_transaction_by_id(
        credit_card_account_id: Annotated[int, Field(description="creditCardAccountId")],
        transaction_id: Annotated[int, Field(description="transactionId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/creditcardaccounts/{creditCardAccountId}/transactions/{transactionId}", path_params={"creditCardAccountId": credit_card_account_id, "transactionId": transaction_id}, query={}, body=None)

    @mcp.tool(name="get_definition_by_id", description="[Custom Fields] Retrieve a custom field definition. Retrieves a specific custom field definition by id. Required permission(s): PermissionGroup > CustomFields - `View`")
    async def get_definition_by_id(
        definition_id: Annotated[int, Field(description="definitionId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/customfields/definitions/{definitionId}", path_params={"definitionId": definition_id}, query={}, body=None)

    @mcp.tool(name="update_patch_custom_field_definition", description="[Custom Fields] Update a custom field definition. Updates a custom field definition. For dropdown definitions, options are reconciled by id: options are added, their text is edited, or they are removed. Reordering existing options (changing their position without changing their text) is not supported and has no effect. The field type of a definition cannot be changed after creation, with one exception: a `ShortText` definition may be upgraded to `LongText`. When replacing the entire `Configuration` object, include its `FieldType` value to indicate which configuration shape is being provided. Required Permission(s): PermissionGroup > CustomFields - `View` `Edit`")
    async def update_patch_custom_field_definition(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        definition_id: Annotated[int, Field(description="definitionId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PATCH", "/v1/customfields/definitions/{definitionId}", path_params={"definitionId": definition_id}, query={}, body=body)

    @mcp.tool(name="delete_custom_field_definition", description="[Custom Fields] Delete a custom field definition. Deletes a custom field definition. Required permission(s): PermissionGroup > CustomFields - `Delete`")
    async def delete_custom_field_definition(
        definition_id: Annotated[int, Field(description="definitionId")],
    ) -> dict[str, Any]:
        return await client.raw_request("DELETE", "/v1/customfields/definitions/{definitionId}", path_params={"definitionId": definition_id}, query={}, body=None)

    @mcp.tool(name="get_definitions_by_entity_type", description="[Custom Fields] Retrieve all custom field definitions for an entity type. Retrieves all custom field definitions for the given entity type, optionally filtered by name, group id, and active state. Required permission(s): PermissionGroup > CustomFields - `View`")
    async def get_definitions_by_entity_type(
        entity_type: Annotated[str, Field(description="entityType")],
        name: Annotated[str | None, Field(description="name")] = None,
        groupid: Annotated[int | None, Field(description="groupid")] = None,
        isactive: Annotated[bool | None, Field(description="isactive")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/customfields/entityType/{entityType}/definitions", path_params={"entityType": entity_type}, query={"name": name, "groupid": groupid, "isactive": isactive}, body=None)

    @mcp.tool(name="create_definition", description="[Custom Fields] Create a custom field definition. Creates a custom field definition for the given entity type (a maximum of 20 definitions can be created per entity type). Required permission(s): PermissionGroup > CustomFields - `View` `Edit`")
    async def create_definition(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        entity_type: Annotated[str, Field(description="entityType")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/customfields/entityType/{entityType}/definitions", path_params={"entityType": entity_type}, query={}, body=body)

    @mcp.tool(name="get_values", description="[Custom Fields] Retrieve custom field values for an entity. Retrieves the custom field values for a specific entity. Required permission(s): PermissionGroup > CustomFields - `View`")
    async def get_values(
        entity_type: Annotated[str, Field(description="entityType")],
        entity_id: Annotated[int, Field(description="entityId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/customfields/entityType/{entityType}/entityId/{entityId}/values", path_params={"entityType": entity_type, "entityId": entity_id}, query={}, body=None)

    @mcp.tool(name="create_upsert_values", description="[Custom Fields] Upsert custom field values for an entity. Creates or updates the custom field values for a specific entity. Required permission(s): PermissionGroup > CustomFields - `View` `Edit`")
    async def create_upsert_values(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        entity_type: Annotated[str, Field(description="entityType")],
        entity_id: Annotated[int, Field(description="entityId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/customfields/entityType/{entityType}/entityId/{entityId}/values", path_params={"entityType": entity_type, "entityId": entity_id}, query={}, body=body)

    @mcp.tool(name="get_groups", description="[Custom Fields] Retrieve all custom field groups for an entity type. Retrieves all custom field groups for the given entity type. Required permission(s): PermissionGroup > CustomFields - `View`")
    async def get_groups(
        entity_type: Annotated[str, Field(description="entityType")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/customfields/entityType/{entityType}/groups", path_params={"entityType": entity_type}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_group", description="[Custom Fields] Create a custom field group. Creates a custom field group for the given entity type. Required permission(s): PermissionGroup > CustomFields - `View` `Edit`")
    async def create_group(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        entity_type: Annotated[str, Field(description="entityType")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/customfields/entityType/{entityType}/groups", path_params={"entityType": entity_type}, query={}, body=body)

    @mcp.tool(name="get_group", description="[Custom Fields] Retrieve a custom field group. Retrieves a custom field group by id. Required permission(s): PermissionGroup > CustomFields - `View`")
    async def get_group(
        group_id: Annotated[int, Field(description="groupId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/customfields/groups/{groupId}", path_params={"groupId": group_id}, query={}, body=None)

    @mcp.tool(name="update_patch_group", description="[Custom Fields] Update a custom field group. Updates a custom field group. Required permission(s): PermissionGroup > CustomFields - `View` `Edit`")
    async def update_patch_group(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        group_id: Annotated[int, Field(description="groupId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PATCH", "/v1/customfields/groups/{groupId}", path_params={"groupId": group_id}, query={}, body=body)

    @mcp.tool(name="get_file_share_settings_by_id", description="[Files] Retrieve file share settings. Retrieves a file's share settings. Note, that the response JSON schema includes share setting fields for all file entity types, however only fields that pertain to the queried file entity type will be populated. For example, if a file of entity type Rental is retrieved only the fields in the Rental section of the response will have values. Required permission(s): Documents > Files - `View`")
    async def get_file_share_settings_by_id(
        file_id: Annotated[int, Field(description="fileId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/files/{fileId}/sharing", path_params={"fileId": file_id}, query={}, body=None)

    @mcp.tool(name="update_file_sharing_setting", description="[Files] Update file share settings. Updates a file's share settings. Note, can only update a file's share settings based on the file's entity type (ie: If the file belongs to a rental property, you can only update the rental file sharing settings). The response payload contains file share setting values for all file entity types, but the relevant setting values correlate to the file's entity type. Required permission(s): Documents > Files - `View` `Edit`")
    async def update_file_sharing_setting(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        file_id: Annotated[int, Field(description="fileId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/files/{fileId}/sharing", path_params={"fileId": file_id}, query={}, body=body)

    @mcp.tool(name="get_file_category_by_id", description="[Files] Retrieve a category. Retrieves a specific file category. Required permission(s): Documents > Files - `View`")
    async def get_file_category_by_id(
        file_category_id: Annotated[int, Field(description="fileCategoryId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/files/categories/{fileCategoryId}", path_params={"fileCategoryId": file_category_id}, query={}, body=None)

    @mcp.tool(name="create_upload_request_async", description="[Files] Upload a file. Uploading a file requires making two API requests. Each step is outlined below. Step 1 - Save file metadata The first step in the file upload process is to submit the file metadata to `/v1/files/uploads`. The response of this call will contain an upload URL and a collection of headers that will be used in step 2 to generate the request for the file binary upload. NOTE: The response data will expire after 5 minutes. The file metadata will not be saved in the Buildium system if step 2 of this process is not completed successfully. Step 2 - Upload the file binary Uploading the file binary will require using the response from step 1 to form a PUT request to the Buildium file provider. Follow these steps to create the request: 1. Form a PUT request using the value of the `UploadUrl` property as the URL. 2. Set the `Content-Type` header to `application/octet-stream`. 3. Copy ...")
    async def create_upload_request_async(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/files/uploads", path_params={}, query={}, body=body)

    @mcp.tool(name="get_general_ledger_entries", description="[General Ledger] Retrieve all general ledger entries. Retrieves all general ledger entries Required permission(s): Accounting > General Ledger Transactions - `View`")
    async def get_general_ledger_entries(
        accountingbasis: Annotated[str, Field(description="The methodology in which revenues and expenses are recognized when calculating the balances. Specifying `Cash` calculates balances based on when money changes hands. Specifying `Accrual` calculates balances based on the period in which the transaction originally happened.")],
        glaccountids: Annotated[list[int], Field(description="Filters results to entries whose general ledger account belongs to the specified set of general ledger account ids.")],
        startdate: Annotated[str, Field(description="Filters results to any entries whose start date is greater than or equal to the specified value.")],
        enddate: Annotated[str, Field(description="Filters results to any entries whose end date is less than or equal to the specified value.")],
        entitytype: Annotated[str | None, Field(description="Specifies the type of entity that `EntityId` field refers to.")] = None,
        entityid: Annotated[int | None, Field(description="Filters results to any general ledger entry containing line items associated with the specified entity identifier. This filter is used in conjunction with the `EntityType` field which must be set to the type of entity this identifier references.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/generalledger", path_params={}, query={"accountingbasis": accountingbasis, "entitytype": entitytype, "entityid": entityid, "glaccountids": glaccountids, "startdate": startdate, "enddate": enddate, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_general_journal_entry", description="[General Ledger] Create a general journal entry. Creates a general journal entry. Required permission(s): Accounting > General Ledger Transactions - `View` `Edit`")
    async def create_general_journal_entry(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/generalledger/journalentries", path_params={}, query={}, body=body)

    @mcp.tool(name="update_general_journal_entry", description="[General Ledger] Update a general journal entry. Updates a general journal entry. Required permission(s): Accounting > General Ledger Transactions - `View` `Edit`")
    async def update_general_journal_entry(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        journal_entry_id: Annotated[int, Field(description="journalEntryId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/generalledger/journalentries/{journalEntryId}", path_params={"journalEntryId": journal_entry_id}, query={}, body=body)

    @mcp.tool(name="get_all_transactions", description="[General Ledger] Retrieve all general ledger transactions. Retrieves a list of general ledger transactions. Required permission(s): Accounting > General Ledger Transactions - `View`")
    async def get_all_transactions(
        startdate: Annotated[str, Field(description="Filters results to any transaction whose date is greater than or equal to the specified value.")],
        enddate: Annotated[str, Field(description="Filters results to any transaction whose date is less than or equal to the specified value.")],
        glaccountids: Annotated[list[int], Field(description="Filters results to transactions whose general ledger account belongs to the specified set of general ledger account ids.")],
        selectionentityid: Annotated[int | None, Field(description="Filters results to any transaction containing journal lines for an entity associated with the specified entity id value. The id must be of the type specified in SelectionEntityType.")] = None,
        selectionentitytype: Annotated[str | None, Field(description="Specifies the type of entity that SelectionEntityId refers to.")] = None,
        selectionentityunitid: Annotated[int | None, Field(description="Filters results to any transaction containing journal lines for the unitId specified. Only applicable when the SelectionEntityType is Rentals or Associations.")] = None,
        lastupdatedfrom: Annotated[str | None, Field(description="Filters results to any transactions that were updated on or after the specified date. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
        lastupdatedto: Annotated[str | None, Field(description="Filters results to any transactions that were updated on or before the specified date. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/generalledger/transactions", path_params={}, query={"selectionentityid": selectionentityid, "selectionentitytype": selectionentitytype, "startdate": startdate, "enddate": enddate, "glaccountids": glaccountids, "selectionentityunitid": selectionentityunitid, "lastupdatedfrom": lastupdatedfrom, "lastupdatedto": lastupdatedto, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_transaction_by_id", description="[General Ledger] Retrieve a general ledger transaction. Retrieves a specific general ledger transaction. Required permission(s): Accounting > General Ledger Transactions - `View`")
    async def get_transaction_by_id(
        transaction_id: Annotated[int, Field(description="The general ledger transaction identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/generalledger/transactions/{transactionId}", path_params={"transactionId": transaction_id}, query={}, body=None)

    @mcp.tool(name="get_all_gl_accounts", description="[General Ledger] Retrieve all general ledger accounts. Retrieves a list of general ledger accounts. General ledger accounts are used to categorize transactions for accounting purposes. Required permission(s): Accounting > General Ledger Accounts - `View`")
    async def get_all_gl_accounts(
        accounttypes: Annotated[list[str] | None, Field(description="Filters results by the specified general ledger account types.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/glaccounts", path_params={}, query={"accounttypes": accounttypes, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_general_ledger_account", description="[General Ledger] Create a general ledger account. Creates a general ledger account. Required permission(s): Accounting > General Ledger Accounts - `View` `Edit`")
    async def create_general_ledger_account(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/glaccounts", path_params={}, query={}, body=body)

    @mcp.tool(name="get_gl_account_by_id", description="[General Ledger] Retrieve a general ledger account. Retrieves a specific general ledger account. Required permission(s): Accounting > General Ledger Accounts - `View`")
    async def get_gl_account_by_id(
        gl_account_id: Annotated[int, Field(description="The general ledger account identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/glaccounts/{glAccountId}", path_params={"glAccountId": gl_account_id}, query={}, body=None)

    @mcp.tool(name="update_gl_account", description="[General Ledger] Update a general ledger account. Updates a general ledger account. Required permission(s): Accounting > General Ledger Accounts - `View` `Edit`")
    async def update_gl_account(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        gl_account_id: Annotated[int, Field(description="glAccountId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/glaccounts/{glAccountId}", path_params={"glAccountId": gl_account_id}, query={}, body=body)

    @mcp.tool(name="get_gl_account_balances", description="[General Ledger] Retrieve all general ledger account balances. Retrieves all general ledger account balances as of a given date. The response includes the total balance of each account along with the subtotals for any accounting entities (company, associations or rental properties) that have transactions assigned to the account. Required permission(s): Accounting > General Ledger Accounts - `View`")
    async def get_gl_account_balances(
        accountingbasis: Annotated[str, Field(description="The methodology in which revenues and expenses are recognized when calculating the balances. Specifying `Cash` calculates balances based on when money changes hands. Specifying `Accrual` calculates balances based on the period in which the transaction originally happened.")],
        asofdate: Annotated[str, Field(description="Indicates the end date through which the balances will be calculated. This will include all transactions in your account until this specified date.")],
        entitytype: Annotated[str | None, Field(description="Specifies the type of entity that `EntityId` field refers to.")] = None,
        entityid: Annotated[int | None, Field(description="Filters transactions used in calculating the general ledger account balances to only those containing journal lines for with the specified entity id value. The entity id specified must be of the type specified in `EntityType`.")] = None,
        glaccountids: Annotated[list[int] | None, Field(description="Filters results to the specified set of general ledger account identifiers.")] = None,
        aggregatebalancesbyunitid: Annotated[bool | None, Field(description="Indicates whether to aggregate the AccountingEntityBalances by unit identifier in the response. If the value is set to true the AccountingEntityBalances will be aggregated by AccountingEntity.Unit.Id otherwise the response will have the balances aggregated by AccountingEntity.Id.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/glaccounts/balances", path_params={}, query={"entitytype": entitytype, "entityid": entityid, "glaccountids": glaccountids, "accountingbasis": accountingbasis, "asofdate": asofdate, "aggregatebalancesbyunitid": aggregatebalancesbyunitid, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_lease_epay_settings_by_id", description="[Leases] Retrieve ePay settings. Retrieves ePay settings for a lease. Required permission(s): Rentals > Leases - `View`")
    async def get_lease_epay_settings_by_id(
        lease_id: Annotated[int, Field(description="leaseId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/{leaseId}/epaysettings", path_params={"leaseId": lease_id}, query={}, body=None)

    @mcp.tool(name="update_lease_epay_settings", description="[Leases] Update ePay settings. Updates ePay settings for a lease Required permission(s): Rentals > Leases - `View` `Edit`")
    async def update_lease_epay_settings(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        lease_id: Annotated[int, Field(description="leaseId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/leases/{leaseId}/epaysettings", path_params={"leaseId": lease_id}, query={}, body=body)

    @mcp.tool(name="get_lease_partial_payment_settings", description="[Leases] Retrieve all partial payment settings for a lease. Retrieves partial payment settings for a lease. Required permission(s): Rentals > Leases - `View`")
    async def get_lease_partial_payment_settings(
        lease_id: Annotated[int, Field(description="leaseId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/{leaseId}/partialpaymentsettings", path_params={"leaseId": lease_id}, query={}, body=None)

    @mcp.tool(name="update_patch_lease_partial_payment_settings", description="[Leases] Update partial payment settings for a lease. Updates partial payment settings for a lease. Required Permission(s): Rentals > Leases - `View` `Edit` Administration > Application Settings - `View` `Edit`")
    async def update_patch_lease_partial_payment_settings(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        lease_id: Annotated[int, Field(description="leaseId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PATCH", "/v1/leases/{leaseId}/partialpaymentsettings", path_params={"leaseId": lease_id}, query={}, body=body)

    @mcp.tool(name="create_lease_charge_recurring_transaction", description="[Lease Transactions] Create a recurring charge. Creates a recurring charge transaction that will post automatically on the specified lease ledger. Required permission(s): Rentals > Lease transactions - `View` `Edit`")
    async def create_lease_charge_recurring_transaction(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        lease_id: Annotated[int, Field(description="leaseId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/leases/{leaseId}/recurringcharges", path_params={"leaseId": lease_id}, query={}, body=body)

    @mcp.tool(name="get_lease_charge_recurring_transaction_by_id", description="[Lease Transactions] Retrieve a recurring charge. Retrieves a recurring charge. Required permission(s): Rentals > Lease transactions - `View`")
    async def get_lease_charge_recurring_transaction_by_id(
        lease_id: Annotated[int, Field(description="leaseId")],
        transaction_id: Annotated[int, Field(description="transactionId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/{leaseId}/recurringcharges/{transactionId}", path_params={"leaseId": lease_id, "transactionId": transaction_id}, query={}, body=None)

    @mcp.tool(name="create_lease_credit_recurring_transaction", description="[Lease Transactions] Create a recurring credit. Creates a recurring credit transaction on the specified lease ledger. Required permission(s): Rentals > Lease transactions - `View` `Edit`")
    async def create_lease_credit_recurring_transaction(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        lease_id: Annotated[int, Field(description="leaseId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/leases/{leaseId}/recurringcredits", path_params={"leaseId": lease_id}, query={}, body=body)

    @mcp.tool(name="get_lease_recurring_credit_by_id", description="[Lease Transactions] Retrieve a recurring credit. Retrieves a recurring credit. Required permission(s): Rentals > Lease transactions - `View`")
    async def get_lease_recurring_credit_by_id(
        lease_id: Annotated[int, Field(description="leaseId")],
        transaction_id: Annotated[int, Field(description="transactionId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/{leaseId}/recurringcredits/{transactionId}", path_params={"leaseId": lease_id, "transactionId": transaction_id}, query={}, body=None)

    @mcp.tool(name="create_lease_recurring_payment", description="[Lease Transactions] Create a recurring payment. Creates a recurring payment that will post automatically on the specified lease ledger. Required permission(s): Rentals > Lease Transactions - `View` `Edit`")
    async def create_lease_recurring_payment(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        lease_id: Annotated[int, Field(description="leaseId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/leases/{leaseId}/recurringpayments", path_params={"leaseId": lease_id}, query={}, body=body)

    @mcp.tool(name="get_recurring_lease_payments_by_id", description="[Lease Transactions] Retrieve a recurring payment. Retrieves a recurring payment. Required permission(s): Rentals > Lease Transactions - `View`")
    async def get_recurring_lease_payments_by_id(
        lease_id: Annotated[int, Field(description="leaseId")],
        payment_id: Annotated[int, Field(description="paymentId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/{leaseId}/recurringpayments/{paymentId}", path_params={"leaseId": lease_id, "paymentId": payment_id}, query={}, body=None)

    @mcp.tool(name="get_rent", description="[Leases] Retrieve all rent schedules. The rent schedule provides details (dollar amount, day of the month, etc) of the recurring charges that are applied to the lease ledger each rent cycle. A lease may have more than one rent schedule associated with it if the rent terms change within the duration of the lease. Required permission(s): Rentals > Lease transactions - `View`")
    async def get_rent(
        lease_id: Annotated[int, Field(description="leaseId")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/{leaseId}/rent", path_params={"leaseId": lease_id}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_rent_schedule", description="[Leases] Create a rent schedule. Creates a rent schedule. Required permission(s): Rentals > Lease Transactions - `View` `Edit`")
    async def create_rent_schedule(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        lease_id: Annotated[int, Field(description="leaseId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/leases/{leaseId}/rent", path_params={"leaseId": lease_id}, query={}, body=body)

    @mcp.tool(name="get_rent_by_id", description="[Leases] Retrieve a rent schedule. Retrieves a specific rent schedule for a lease. The rent schedule provides details (dollar amount, day of the month, etc) of the recurring charges that are applied to the lease ledger each rent cycle. Required permission(s): Rentals > Lease transactions - `View`")
    async def get_rent_by_id(
        lease_id: Annotated[int, Field(description="leaseId")],
        rent_id: Annotated[int, Field(description="rentId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/{leaseId}/rent/{rentId}", path_params={"leaseId": lease_id, "rentId": rent_id}, query={}, body=None)

    @mcp.tool(name="update_rent_schedule", description="[Leases] Update a rent schedule. Updates a rent schedule. Required permission(s): Rentals > Lease Transactions - `View` `Edit`")
    async def update_rent_schedule(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        lease_id: Annotated[int, Field(description="leaseId")],
        rent_id: Annotated[int, Field(description="rentId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/leases/{leaseId}/rent/{rentId}", path_params={"leaseId": lease_id, "rentId": rent_id}, query={}, body=body)

    @mcp.tool(name="get_renters_insurance_policies", description="[Leases] Retrieve all insurance policies. Retrieves all renters insurance policies for a lease. Required permission(s): Rentals > Leases - `View`")
    async def get_renters_insurance_policies(
        lease_id: Annotated[int, Field(description="leaseId")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/{leaseId}/rentersinsurance", path_params={"leaseId": lease_id}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_renters_insurance_policy_by_id", description="[Leases] Retrieve an insurance policy. Retrieves a renters insurance policy. Required permission(s): Rentals > Leases - `View`")
    async def get_renters_insurance_policy_by_id(
        lease_id: Annotated[int, Field(description="leaseId")],
        policy_id: Annotated[int, Field(description="policyId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/{leaseId}/rentersinsurance/{policyId}", path_params={"leaseId": lease_id, "policyId": policy_id}, query={}, body=None)

    @mcp.tool(name="get_recurring_transactions_for_all_leases", description="[Lease Transactions] Retrieve all recurring transactions for all leases. Retrieves all recurring transactions for all leases. Required permission(s): Rentals > Lease transactions - `View`")
    async def get_recurring_transactions_for_all_leases(
        leaseids: Annotated[list[int] | None, Field(description="Filters results to only include records associated with the provided lease Ids.")] = None,
        createddatetimefrom: Annotated[str | None, Field(description="Filters results to recurring transactions created after the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. The maximum date range is 365 days.")] = None,
        createddatetimeto: Annotated[str | None, Field(description="Filters results to recurring transactions created before the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. The maximum date range is 365 days.")] = None,
        lastupdatedfrom: Annotated[str | None, Field(description="Filters results to recurring transactions last updated after the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. The maximum date range is 365 days.")] = None,
        lastupdatedto: Annotated[str | None, Field(description="Filters results to recurring transactions last updated before the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. The maximum date range is 365 days.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/recurringtransactions", path_params={}, query={"leaseids": leaseids, "createddatetimefrom": createddatetimefrom, "createddatetimeto": createddatetimeto, "lastupdatedfrom": lastupdatedfrom, "lastupdatedto": lastupdatedto, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_lease_renewal_history", description="[Leases] Retrieve all lease renewal history. Retrieves all lease renewal history Required permission(s): Rentals > Leases - `View`")
    async def get_lease_renewal_history(
        leaseids: Annotated[list[int] | None, Field(description="Filters results to only include lease renewals whose renewals belongs to the specified set of lease ids.")] = None,
        createddatetimefrom: Annotated[str | None, Field(description="Filters results to only lease renewals that were created after this date. The value must be in UTC and formatted as `YYYY-MM-DDTHH:MM:SSZ`. The maximum date range is 365 days.")] = None,
        createddatetimeto: Annotated[str | None, Field(description="Filters results to only lease renewals that were created before this date.The value must be in UTC and formatted as `YYYY-MM-DDTHH:MM:SSZ`. The maximum date range is 365 days.")] = None,
        lastupdatedfrom: Annotated[str | None, Field(description="Filters results to any lease renewals that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. The maximum date range is 365 days.")] = None,
        lastupdatedto: Annotated[str | None, Field(description="Filters results to any lease renewals were updated on or before the specified date.The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. The maximum date range is 365 days.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/renewalhistory", path_params={}, query={"leaseids": leaseids, "createddatetimefrom": createddatetimefrom, "createddatetimeto": createddatetimeto, "lastupdatedfrom": lastupdatedfrom, "lastupdatedto": lastupdatedto, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_rent_paged", description="[Leases] Retrieve all rent schedules. The rent schedule provides details (dollar amount, day of the month, etc) of the recurring charges that are applied to the lease ledger each rent cycle. A lease may have more than one rent schedule associated with it if the rent terms change within the duration of the lease. Required permission(s): Rentals > Lease transactions - `View`")
    async def get_rent_paged(
        leaseids: Annotated[list[int] | None, Field(description="Filters results to only include rents whose lease belongs to the specified set of lease ids.")] = None,
        createddatetimefrom: Annotated[str | None, Field(description="Filters results to only rents that were created after this date. The value must be in UTC and formatted as `YYYY-MM-DDTHH:MM:SSZ`. The maximum date range is 365 days.")] = None,
        createddatetimeto: Annotated[str | None, Field(description="Filters results to only rents that were created before this date.The value must be in UTC and formatted as `YYYY-MM-DDTHH:MM:SSZ`. The maximum date range is 365 days.")] = None,
        lastupdatedfrom: Annotated[str | None, Field(description="Filters results to any rents that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. The maximum date range is 365 days.")] = None,
        lastupdatedto: Annotated[str | None, Field(description="Filters results to any rents were updated on or before the specified date.The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. The maximum date range is 365 days.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/rent", path_params={}, query={"leaseids": leaseids, "createddatetimefrom": createddatetimefrom, "createddatetimeto": createddatetimeto, "lastupdatedfrom": lastupdatedfrom, "lastupdatedto": lastupdatedto, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_all_tenant_notes", description="[Rental Tenants] Retrieve all notes. Retrieves all tenant notes. Required permission(s): Rentals > Tenants - `View`")
    async def get_all_tenant_notes(
        tenant_id: Annotated[int, Field(description="The tenant identifier.")],
        updateddatetimefrom: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        updateddatetimeto: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        lastupdatedbyuserid: Annotated[int | None, Field(description="Filters results to only notes that were last updated by the specified user identifier.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/tenants/{tenantId}/notes", path_params={"tenantId": tenant_id}, query={"updateddatetimefrom": updateddatetimefrom, "updateddatetimeto": updateddatetimeto, "lastupdatedbyuserid": lastupdatedbyuserid, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_tenant_note", description="[Rental Tenants] Create a note. Creates a tenant note. Required permission(s): Rentals > Tenants - `View` `Edit`")
    async def create_tenant_note(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        tenant_id: Annotated[int, Field(description="tenantId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/leases/tenants/{tenantId}/notes", path_params={"tenantId": tenant_id}, query={}, body=body)

    @mcp.tool(name="get_tenant_note_by_id", description="[Rental Tenants] Retrieve a note. Retrieves a tenant note. Required permission(s): Rentals > Tenants - `View`")
    async def get_tenant_note_by_id(
        tenant_id: Annotated[int, Field(description="tenantId")],
        note_id: Annotated[int, Field(description="noteId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/leases/tenants/{tenantId}/notes/{noteId}", path_params={"tenantId": tenant_id, "noteId": note_id}, query={}, body=None)

    @mcp.tool(name="update_lease_tenant_note", description="[Rental Tenants] Update a note. Updates a tenant note. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Rentals > Tenants - `View` `Edit`")
    async def update_lease_tenant_note(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        tenant_id: Annotated[int, Field(description="tenantId")],
        note_id: Annotated[int, Field(description="noteId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/leases/tenants/{tenantId}/notes/{noteId}", path_params={"tenantId": tenant_id, "noteId": note_id}, query={}, body=body)

    @mcp.tool(name="get_property_groups", description="[Property Groups] Retrieve all property groups. Retrieves all property groups. Required permission(s): Rentals > Rental properties and units or - `View` Associations > Associations and units - `View`")
    async def get_property_groups(
        propertyids: Annotated[list[int] | None, Field(description="Filters results to property groups that contain any of the specified property ids.")] = None,
        nameordescription: Annotated[str | None, Field(description="Filters results to any property group whose name or description contains the specified value.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/propertygroups", path_params={}, query={"propertyids": propertyids, "nameordescription": nameordescription, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_property_group", description="[Property Groups] Create a property group. Creates a property group. Required permission(s): Rentals > Rental properties and units or - `View` `Edit` Associations > Associations and units - `View` `Edit`")
    async def create_property_group(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/propertygroups", path_params={}, query={}, body=body)

    @mcp.tool(name="get_property_group_by_id", description="[Property Groups] Retrieve a property group. Retrieves a property group. Required permission(s): Rentals > Rental properties and units or - `View` Associations > Associations and units - `View`")
    async def get_property_group_by_id(
        property_group_id: Annotated[int, Field(description="propertyGroupId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/propertygroups/{propertyGroupId}", path_params={"propertyGroupId": property_group_id}, query={}, body=None)

    @mcp.tool(name="update_property_group", description="[Property Groups] Update a property group. Updates a property group. A property group can only be updated by the user that created it. Required permission(s): Rentals > Rental properties and units or - `View` `Edit` Associations > Associations and units - `View` `Edit`")
    async def update_property_group(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        property_group_id: Annotated[int, Field(description="propertyGroupId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/propertygroups/{propertyGroupId}", path_params={"propertyGroupId": property_group_id}, query={}, body=body)

    @mcp.tool(name="get_features_by_rental_property_id", description="[Rental Properties] Retrieve all amenities. Retrieve all the amenities for a rental property. Required permission(s): Rentals > Rental properties and units - `View`")
    async def get_features_by_rental_property_id(
        property_id: Annotated[int, Field(description="propertyId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/rentals/{propertyId}/amenities", path_params={"propertyId": property_id}, query={}, body=None)

    @mcp.tool(name="update_rental_features", description="[Rental Properties] Update amenities. Updates the amenities for a rental property. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Rentals > Rental properties and units - `View` `Edit`")
    async def update_rental_features(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        property_id: Annotated[int, Field(description="propertyId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/rentals/{propertyId}/amenities", path_params={"propertyId": property_id}, query={}, body=body)

    @mcp.tool(name="get_e_pay_settings_for_rental_property", description="[Rental Properties] Retrieve ePay settings. Retrieves ePay settings for a rental property. Required permission(s): Rentals > Rental properties and units - `View`")
    async def get_e_pay_settings_for_rental_property(
        property_id: Annotated[int, Field(description="propertyId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/rentals/{propertyId}/epaysettings", path_params={"propertyId": property_id}, query={}, body=None)

    @mcp.tool(name="update_e_pay_settings_for_rental", description="[Rental Properties] Update ePay settings. Updates ePay settings for a rental property. Required permission(s): Rentals > Rental properties and units - `View` `Edit`")
    async def update_e_pay_settings_for_rental(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        property_id: Annotated[int, Field(description="propertyId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/rentals/{propertyId}/epaysettings", path_params={"propertyId": property_id}, query={}, body=body)

    @mcp.tool(name="get_rental_images", description="[Rental Properties] Retrieve all property images. Retrieves all images for a rental property. Note this endpoint will only return file metadata such as file names and descriptions. To download files make requests to the [Download File](#tag/Rental-Properties/operation/ExternalApiRentalImageDownloadRequests_GetRentalImageDownloadUrlById) endpoint. Required permission(s): Rentals > Rental properties and units - `View`")
    async def get_rental_images(
        property_id: Annotated[int, Field(description="propertyId")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/rentals/{propertyId}/images", path_params={"propertyId": property_id}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_rental_image_by_id", description="[Rental Properties] Retrieve a property image. Retrieves a rental property image. Required permission(s): Rentals > Rental properties and units - `View`")
    async def get_rental_image_by_id(
        property_id: Annotated[int, Field(description="propertyId")],
        image_id: Annotated[int, Field(description="imageId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/rentals/{propertyId}/images/{imageId}", path_params={"propertyId": property_id, "imageId": image_id}, query={}, body=None)

    @mcp.tool(name="update_rental_image", description="[Rental Properties] Update a property image. Updates a rental property image. Required permission(s): Rentals > Rental properties and units - `View` `Edit`")
    async def update_rental_image(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        property_id: Annotated[int, Field(description="propertyId")],
        image_id: Annotated[int, Field(description="imageId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/rentals/{propertyId}/images/{imageId}", path_params={"propertyId": property_id, "imageId": image_id}, query={}, body=body)

    @mcp.tool(name="delete_rental_image", description="[Rental Properties] Delete a property image. Deletes a rental property image. Required permission(s): Rentals > Rental properties and units - `View` `Edit` `Delete`")
    async def delete_rental_image(
        property_id: Annotated[int, Field(description="propertyId")],
        image_id: Annotated[int, Field(description="imageId")],
    ) -> dict[str, Any]:
        return await client.raw_request("DELETE", "/v1/rentals/{propertyId}/images/{imageId}", path_params={"propertyId": property_id, "imageId": image_id}, query={}, body=None)

    @mcp.tool(name="create_get_rental_image_download_url_by_id", description="[Rental Properties] Download a property image. Use this endpoint to create a temporary URL that can be used to download a property image. This URL expires after 5 minutes. Required permission(s): Rentals > Rental properties and units - `View`")
    async def create_get_rental_image_download_url_by_id(
        property_id: Annotated[int, Field(description="propertyId")],
        image_id: Annotated[int, Field(description="imageId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/rentals/{propertyId}/images/{imageId}/downloadrequests", path_params={"propertyId": property_id, "imageId": image_id}, query={}, body=None)

    @mcp.tool(name="update_reorder_rental_images", description="[Rental Properties] Update property image order. Updates the image display order within the Buildium web application and in any associated rental listings. Required permission(s): Rentals > Rental properties and units - `View` `Edit`")
    async def update_reorder_rental_images(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        property_id: Annotated[int, Field(description="propertyId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/rentals/{propertyId}/images/order", path_params={"propertyId": property_id}, query={}, body=body)

    @mcp.tool(name="create_upload_request_async_rental_properties", description="[Rental Properties] Upload a rental image. Uploading a file requires making two API requests. Each step is outlined below. Step 1 - Save file metadata The first step in the file upload process is to submit the file metadata to `/v1/rentals/{propertyId}/images/uploads`. The response of this call will contain an upload URL and a collection of headers that will be used in step 2 to generate the request for the file binary upload. NOTE: The response data will expire after 5 minutes. The file metadata will not be saved in the Buildium system if step 2 of this process is not completed successfully. Step 2 - Upload the file binary Uploading the file binary will require using the response from step 1 to form a PUT request to the Buildium file provider. Follow these steps to create the request: 1. Form a PUT request using the value of the `UploadUrl` property as the URL. 2. Set the `Content-Type` header to `appli...")
    async def create_upload_request_async_rental_properties(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        property_id: Annotated[int, Field(description="propertyId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/rentals/{propertyId}/images/uploads", path_params={"propertyId": property_id}, query={}, body=body)

    @mcp.tool(name="create_video_link_request", description="[Rental Properties] Create an image for a rental using a video link. Creates an image for a rental using a video link. Required permission(s): Rentals > Rental properties and units - `View` `Edit`")
    async def create_video_link_request(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        property_id: Annotated[int, Field(description="propertyId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/rentals/{propertyId}/images/videolinkrequests", path_params={"propertyId": property_id}, query={}, body=body)

    @mcp.tool(name="get_meter_readings_for_rental", description="[Rental Meter Readings] Retrieve all meter readings. Retrieves all meter readings for a rental property. Required permission(s): Rentals > Rental properties and units - `View`")
    async def get_meter_readings_for_rental(
        property_id: Annotated[int, Field(description="propertyId")],
        readingdatefrom: Annotated[str, Field(description="Filters results to any meter readings whose entry date that is greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD. The maximum date range is 365 days.")],
        readingdateto: Annotated[str, Field(description="Filters results to any meter readings whose entry date is less than or equal to the specified value. The value must be formatted as YYYY-MM-DD. The maximum date range is 365 days.")],
        metertypes: Annotated[list[str] | None, Field(description="Filters results to the specified meter types.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/rentals/{propertyId}/meterreadings", path_params={"propertyId": property_id}, query={"readingdatefrom": readingdatefrom, "readingdateto": readingdateto, "metertypes": metertypes, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_meter_reading_details_for_rental_async", description="[Rental Meter Readings] Retrieve all meter reading details. Retrieves all meter reading details for a property. Required permission(s): Rentals > Rental properties and units - `View`")
    async def get_meter_reading_details_for_rental_async(
        property_id: Annotated[int, Field(description="propertyId")],
        readingdate: Annotated[str, Field(description="Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD.")],
        metertype: Annotated[str, Field(description="Filters results to the specified meter type.")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/rentals/{propertyId}/meterreadings/summary", path_params={"propertyId": property_id}, query={"readingdate": readingdate, "metertype": metertype}, body=None)

    @mcp.tool(name="update_upsert_meter_reading_details_for_rental_async", description="[Rental Meter Readings] Create/Update meter reading details. This endpoint can be used to both create and update a meter reading detail for a property. There can only be one meter reading detail for a given combination of MeterType and ReadingDate for a property. If you are updating an existing meter reading detail, use the query parameters to specify the existing meter reading detail to update. If you are creating a new meter reading detail, do not pass any query parameters. When adding a new item to the Details array, leave out the `Id` field. When updating an existing item in the Details array, the `Id` field of the existing item must be included. Required permission(s): Rentals > Rental properties and units - `View` `Edit`")
    async def update_upsert_meter_reading_details_for_rental_async(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        property_id: Annotated[int, Field(description="propertyId")],
        readingdate: Annotated[str | None, Field(description="Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD.")] = None,
        metertype: Annotated[str | None, Field(description="Filters results to the specified meter type.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/rentals/{propertyId}/meterreadings/summary", path_params={"propertyId": property_id}, query={"readingdate": readingdate, "metertype": metertype}, body=body)

    @mcp.tool(name="delete_meter_reading_details_for_rental", description="[Rental Meter Readings] Delete meter reading details for a given date. Delete meter reading details for a property for a given date. Required permission(s): Rentals > Lease Transactions - `View` `Edit` `Delete`")
    async def delete_meter_reading_details_for_rental(
        property_id: Annotated[int, Field(description="propertyId")],
        readingdate: Annotated[str, Field(description="Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD.")],
        metertype: Annotated[str, Field(description="Filters results to the specified meter type.")],
    ) -> dict[str, Any]:
        return await client.raw_request("DELETE", "/v1/rentals/{propertyId}/meterreadings/summary", path_params={"propertyId": property_id}, query={"readingdate": readingdate, "metertype": metertype}, body=None)

    @mcp.tool(name="get_rental_notes", description="[Rental Properties] Retrieve all notes. Retrieves all notes. Required permission(s): Rentals > Rental properties and units - `View`")
    async def get_rental_notes(
        property_id: Annotated[int, Field(description="propertyId")],
        updateddatetimefrom: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        updateddatetimeto: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        lastupdatedbyuserid: Annotated[int | None, Field(description="Filters results to only notes that were last updated by the specified user identifier.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/rentals/{propertyId}/notes", path_params={"propertyId": property_id}, query={"updateddatetimefrom": updateddatetimefrom, "updateddatetimeto": updateddatetimeto, "lastupdatedbyuserid": lastupdatedbyuserid, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_rental_property_note", description="[Rental Properties] Create a note. Creates a note. Required permission(s): Rentals > Rental properties and units - `View` `Edit`")
    async def create_rental_property_note(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        property_id: Annotated[int, Field(description="propertyId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/rentals/{propertyId}/notes", path_params={"propertyId": property_id}, query={}, body=body)

    @mcp.tool(name="get_rental_note_by_note_id", description="[Rental Properties] Retrieve a note. Retrieves a note. Required permission(s): Rentals > Rental properties and units - `View`")
    async def get_rental_note_by_note_id(
        property_id: Annotated[int, Field(description="propertyId")],
        note_id: Annotated[int, Field(description="noteId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/rentals/{propertyId}/notes/{noteId}", path_params={"propertyId": property_id, "noteId": note_id}, query={}, body=None)

    @mcp.tool(name="update_rental_property_note", description="[Rental Properties] Update a note. Updates a note. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Rentals > Rental properties and units - `View` `Edit`")
    async def update_rental_property_note(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        property_id: Annotated[int, Field(description="propertyId")],
        note_id: Annotated[int, Field(description="noteId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/rentals/{propertyId}/notes/{noteId}", path_params={"propertyId": property_id, "noteId": note_id}, query={}, body=body)

    @mcp.tool(name="get_rental_appliances", description="[Rental Appliances] Retrieve all appliances. **\u26a0 Deprecated:** This endpoint is deprecated and will start returning **410 Gone** on 2026-10-19. Use `GET /v1/inventoryassets` instead. Appliances have moved to the new Inventory & Assets API. Retrieves all rental appliances. Required permission(s): Rentals > Rental properties and units - `View`")
    async def get_rental_appliances(
        propertyids: Annotated[list[int] | None, Field(description="Filters results to appliances associated to any of the specified rental property identifiers.")] = None,
        unitids: Annotated[list[int] | None, Field(description="Filters results to appliances associated to any of the specified rental unit identifiers.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/rentals/appliances", path_params={}, query={"propertyids": propertyids, "unitids": unitids, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_rental_appliance", description="[Rental Appliances] Create an appliance. **\u26a0 Deprecated:** This endpoint is deprecated and will start returning **410 Gone** on 2026-10-19. Use `POST /v1/inventoryasset` instead. Appliances have moved to the new Inventory & Assets API. Creates a rental property appliance. Required permission(s): Rentals > Rental properties and units - `View` `Edit`")
    async def create_rental_appliance(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/rentals/appliances", path_params={}, query={}, body=body)

    @mcp.tool(name="get_rental_appliance_by_id", description="[Rental Appliances] Retrieve an appliance. **\u26a0 Deprecated:** This endpoint is deprecated and will start returning **410 Gone** on 2026-10-19. Use `GET /v1/inventoryasset/{inventoryAssetId}` instead. Appliances have moved to the new Inventory & Assets API. Retrieves a rental appliance. Required permission(s): Rentals > Rental properties and units - `View`")
    async def get_rental_appliance_by_id(
        appliance_id: Annotated[int, Field(description="applianceId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/rentals/appliances/{applianceId}", path_params={"applianceId": appliance_id}, query={}, body=None)

    @mcp.tool(name="update_rental_appliance", description="[Rental Appliances] Update an appliance. **\u26a0 Deprecated:** This endpoint is deprecated and will start returning **410 Gone** on 2026-10-19. Use `PUT /v1/inventoryasset/{inventoryAssetId}` instead. Appliances have moved to the new Inventory & Assets API. Updates a rental appliance. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Rentals > Rental properties and units - `View` `Edit`")
    async def update_rental_appliance(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        appliance_id: Annotated[int, Field(description="applianceId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/rentals/appliances/{applianceId}", path_params={"applianceId": appliance_id}, query={}, body=body)

    @mcp.tool(name="delete_rental_appliances", description="[Rental Appliances] Delete an appliance. **\u26a0 Deprecated:** This endpoint is deprecated and will start returning **410 Gone** on 2026-10-19. Use `DELETE /v1/inventoryasset/{inventoryAssetId}` instead. Appliances have moved to the new Inventory & Assets API. Deletes an appliance. Required permission(s): Rentals > Rental properties and units - `View` `Edit`")
    async def delete_rental_appliances(
        appliance_id: Annotated[int, Field(description="applianceId")],
    ) -> dict[str, Any]:
        return await client.raw_request("DELETE", "/v1/rentals/appliances/{applianceId}", path_params={"applianceId": appliance_id}, query={}, body=None)

    @mcp.tool(name="get_rental_appliance_service_history", description="[Rental Appliances] Retrieve all service history. **\u26a0 Deprecated:** This endpoint is deprecated and will start returning **410 Gone** on 2026-10-19. Use `GET /v1/assetservicehistory/{inventoryAssetId}` instead. Appliances have moved to the new Inventory & Assets API. Retrieves all of the service history records for an appliance. Required permission(s): Rentals > Rental properties and units - `View`")
    async def get_rental_appliance_service_history(
        appliance_id: Annotated[int, Field(description="applianceId")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/rentals/appliances/{applianceId}/servicehistory", path_params={"applianceId": appliance_id}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_rental_appliance_service_history", description="[Rental Appliances] Create a service history. **\u26a0 Deprecated:** This endpoint is deprecated and will start returning **410 Gone** on 2026-10-19. Use `POST /v1/assetservicehistory/{inventoryAssetId}` instead. Appliances have moved to the new Inventory & Assets API. Creates a service history record for an appliance. Required permission(s): Rentals > Rental properties and units - `View` `Edit`")
    async def create_rental_appliance_service_history(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        appliance_id: Annotated[int, Field(description="applianceId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/rentals/appliances/{applianceId}/servicehistory", path_params={"applianceId": appliance_id}, query={}, body=body)

    @mcp.tool(name="get_rental_appliance_service_history_by_id", description="[Rental Appliances] Retrieve a service history. **\u26a0 Deprecated:** This endpoint is deprecated and will start returning **410 Gone** on 2026-10-19. Use `GET /v1/assetservicehistory/{inventoryAssetId}/{assetServiceHistoryId}` instead. Appliances have moved to the new Inventory & Assets API. Retrieves a specific service history record for a given appliance. Required permission(s): Rentals > Rental properties and units - `View`")
    async def get_rental_appliance_service_history_by_id(
        appliance_id: Annotated[int, Field(description="applianceId")],
        service_history_id: Annotated[int, Field(description="serviceHistoryId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/rentals/appliances/{applianceId}/servicehistory/{serviceHistoryId}", path_params={"applianceId": appliance_id, "serviceHistoryId": service_history_id}, query={}, body=None)

    @mcp.tool(name="get_rental_owner_notes", description="[Rental Owners] Retrieves all notes. Retrieves all rental owner notes. Required permission(s): Rentals > Property Rental Owners - `View`")
    async def get_rental_owner_notes(
        rental_owner_id: Annotated[int, Field(description="rentalOwnerId")],
        updateddatetimefrom: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        updateddatetimeto: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        lastupdatedbyuserid: Annotated[int | None, Field(description="Filters results to only notes that were last updated by the specified user identifier.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/rentals/owners/{rentalOwnerId}/notes", path_params={"rentalOwnerId": rental_owner_id}, query={"updateddatetimefrom": updateddatetimefrom, "updateddatetimeto": updateddatetimeto, "lastupdatedbyuserid": lastupdatedbyuserid, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_rental_owner_note", description="[Rental Owners] Create a note. Creates a new Rental Owner note. Required permission(s): Rentals > Property Rental Owners - `View` `Edit`")
    async def create_rental_owner_note(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        rental_owner_id: Annotated[int, Field(description="rentalOwnerId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/rentals/owners/{rentalOwnerId}/notes", path_params={"rentalOwnerId": rental_owner_id}, query={}, body=body)

    @mcp.tool(name="get_rental_owner_note_by_id", description="[Rental Owners] Retrieve a note. Retrieves a rental owner note. Required permission(s): Rentals > Property Rental Owners - `View`")
    async def get_rental_owner_note_by_id(
        rental_owner_id: Annotated[int, Field(description="rentalOwnerId")],
        note_id: Annotated[int, Field(description="noteId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/rentals/owners/{rentalOwnerId}/notes/{noteId}", path_params={"rentalOwnerId": rental_owner_id, "noteId": note_id}, query={}, body=None)

    @mcp.tool(name="update_rental_owner_note", description="[Rental Owners] Update a note. Updates a Rental Owner note. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Rentals > Property Rental Owners - `View` `Edit`")
    async def update_rental_owner_note(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        rental_owner_id: Annotated[int, Field(description="rentalOwnerId")],
        note_id: Annotated[int, Field(description="noteId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/rentals/owners/{rentalOwnerId}/notes/{noteId}", path_params={"rentalOwnerId": rental_owner_id, "noteId": note_id}, query={}, body=body)

    @mcp.tool(name="get_features_for_rental_unit_by_id", description="[Rental Units] Retrieve all amenities. Retrieves all amenities for a rental unit. Required permission(s): Rentals > Rental properties and units - `View`")
    async def get_features_for_rental_unit_by_id(
        unit_id: Annotated[int, Field(description="unitId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/rentals/units/{unitId}/amenities", path_params={"unitId": unit_id}, query={}, body=None)

    @mcp.tool(name="update_rental_unit_features", description="[Rental Units] Update amenities. Updates the amenities for a rental unit. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Rentals > Rental properties and units - `View` `Edit`")
    async def update_rental_unit_features(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        unit_id: Annotated[int, Field(description="unitId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/rentals/units/{unitId}/amenities", path_params={"unitId": unit_id}, query={}, body=body)

    @mcp.tool(name="get_rental_unit_images", description="[Rental Units] Retrieve all unit images. Retrieves all images for a unit. Note this endpoint will only return file metadata such as file names and descriptions. To download files make requests to the [Download File](#tag/Rental-Units/operation/ExternalApiRentalUnitImageDownloadRequests_GetRentalUnitImageDownloadUrlById) endpoint. Required permission(s): Rentals > Rental properties and units - `View`")
    async def get_rental_unit_images(
        unit_id: Annotated[int, Field(description="unitId")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/rentals/units/{unitId}/images", path_params={"unitId": unit_id}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_rental_unit_image_by_id", description="[Rental Units] Retrieve a unit image. Retrieves a unit image. Required permission(s): Rentals > Rental properties and units - `View`")
    async def get_rental_unit_image_by_id(
        unit_id: Annotated[int, Field(description="unitId")],
        image_id: Annotated[int, Field(description="imageId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/rentals/units/{unitId}/images/{imageId}", path_params={"unitId": unit_id, "imageId": image_id}, query={}, body=None)

    @mcp.tool(name="update_rental_unit_image", description="[Rental Units] Update a unit image. Updates a unit image. Required permission(s): Rentals > Properties and units - `View` `Edit`")
    async def update_rental_unit_image(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        unit_id: Annotated[int, Field(description="unitId")],
        image_id: Annotated[int, Field(description="imageId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/rentals/units/{unitId}/images/{imageId}", path_params={"unitId": unit_id, "imageId": image_id}, query={}, body=body)

    @mcp.tool(name="delete_rental_unit_image", description="[Rental Units] Delete a unit image. Deletes a unit image. Required permission(s): Rentals > Rental properties and units - `View` `Edit` `Delete`")
    async def delete_rental_unit_image(
        unit_id: Annotated[int, Field(description="unitId")],
        image_id: Annotated[int, Field(description="imageId")],
    ) -> dict[str, Any]:
        return await client.raw_request("DELETE", "/v1/rentals/units/{unitId}/images/{imageId}", path_params={"unitId": unit_id, "imageId": image_id}, query={}, body=None)

    @mcp.tool(name="create_get_rental_unit_image_download_url_by_id", description="[Rental Units] Download a unit image. Use this endpoint to create a temporary URL that can be used to download a unit image. This URL expires after 5 minutes. Required permission(s): Rentals > Rental properties and units - `View`")
    async def create_get_rental_unit_image_download_url_by_id(
        unit_id: Annotated[int, Field(description="unitId")],
        image_id: Annotated[int, Field(description="imageId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/rentals/units/{unitId}/images/{imageId}/downloadrequests", path_params={"unitId": unit_id, "imageId": image_id}, query={}, body=None)

    @mcp.tool(name="update_reorder_rental_unit_images", description="[Rental Units] Update unit image order. Updates the image display order within the Buildium web application and in any associated rental listings. Required permission(s): Rentals > Rental properties and units - `View` `Edit`")
    async def update_reorder_rental_unit_images(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        unit_id: Annotated[int, Field(description="unitId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/rentals/units/{unitId}/images/order", path_params={"unitId": unit_id}, query={}, body=body)

    @mcp.tool(name="create_upload_request_async_rental_units", description="[Rental Units] Upload a unit image. Uploading a file requires making two API requests. Each step is outlined below. Step 1 - Save file metadata The first step in the file upload process is to submit the file metadata to `/v1/rentals/units/{unitId}/images/uploads`. The response of this call will contain an upload URL and a collection of headers that will be used in step 2 to generate the request for the file binary upload. NOTE: The response data will expire after 5 minutes. The file metadata will not be saved in the Buildium system if step 2 of this process is not completed successfully. Step 2 - Upload the file binary Uploading the file binary will require using the response from step 1 to form a PUT request to the Buildium file provider. Follow these steps to create the request: 1. Form a PUT request using the value of the `UploadUrl` property as the URL. 2. Set the `Content-Type` header to `appli...")
    async def create_upload_request_async_rental_units(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        unit_id: Annotated[int, Field(description="unitId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/rentals/units/{unitId}/images/uploads", path_params={"unitId": unit_id}, query={}, body=body)

    @mcp.tool(name="create_unit_video_link_request", description="[Rental Units] Create an image for a unit using a video link. Creates an image for a rental unit using a video link. Required permission(s): Rentals > Properties and units - `View` `Edit`")
    async def create_unit_video_link_request(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        unit_id: Annotated[int, Field(description="unitId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/rentals/units/{unitId}/images/videolinkrequests", path_params={"unitId": unit_id}, query={}, body=body)

    @mcp.tool(name="get_rental_unit_notes", description="[Rental Units] Retrieve all notes. Retrieves all rental unit notes. Required permission(s): Rentals > Rental properties and units - `View`")
    async def get_rental_unit_notes(
        unit_id: Annotated[int, Field(description="unitId")],
        updateddatetimefrom: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        updateddatetimeto: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        lastupdatedbyuserid: Annotated[int | None, Field(description="Filters results to only notes that were last updated by the specified user identifier.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/rentals/units/{unitId}/notes", path_params={"unitId": unit_id}, query={"updateddatetimefrom": updateddatetimefrom, "updateddatetimeto": updateddatetimeto, "lastupdatedbyuserid": lastupdatedbyuserid, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_rental_unit_note", description="[Rental Units] Create a note. Creates a rental unit note. Required permission(s): Rentals > Rental properties and units - `View` `Edit`")
    async def create_rental_unit_note(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        unit_id: Annotated[int, Field(description="unitId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/rentals/units/{unitId}/notes", path_params={"unitId": unit_id}, query={}, body=body)

    @mcp.tool(name="get_rental_unit_note_by_note_id", description="[Rental Units] Retrieve a note. Retrieves a rental unit note. Required permission(s): Rentals > Rental properties and units - `View`")
    async def get_rental_unit_note_by_note_id(
        unit_id: Annotated[int, Field(description="unitId")],
        note_id: Annotated[int, Field(description="noteId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/rentals/units/{unitId}/notes/{noteId}", path_params={"unitId": unit_id, "noteId": note_id}, query={}, body=None)

    @mcp.tool(name="update_note_for_rental_unit", description="[Rental Units] Update a note. Updates a rental unit note. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Rentals > Rental properties and units - `View` `Edit`")
    async def update_note_for_rental_unit(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        unit_id: Annotated[int, Field(description="unitId")],
        note_id: Annotated[int, Field(description="noteId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/rentals/units/{unitId}/notes/{noteId}", path_params={"unitId": unit_id, "noteId": note_id}, query={}, body=body)

    @mcp.tool(name="get_resident_center_users", description="[Resident Center] Retrieve all resident center users. Retrieves all resident center users for both rentals and associations. Required permission(s): Communications > Resident Center Users - `View` Rentals > Tenants - `View` is required to retrieve resident center users that are tenants. Associations > Association owners and tenants - `View` is required to retrieve resident center users that are association owners.")
    async def get_resident_center_users(
        unitagreementids: Annotated[list[int] | None, Field(description="Filters results to any resident center user who is associated with the specified lease and/or association ownership account identifiers.")] = None,
        userids: Annotated[list[int] | None, Field(description="Filters results to any resident center user with the specified tenant and/or association owner identifiers.")] = None,
        usertypes: Annotated[list[str] | None, Field(description="Filters results to any resident center user with the specified types.")] = None,
        residentcenteruserstatuses: Annotated[list[str] | None, Field(description="Filters results to any resident center user with the specified resident center user statuses.")] = None,
        isautopayenabled: Annotated[bool | None, Field(description="If true, filters results to any resident center users who have automatic payments scheduled for the future. If false, filters results to any resident center users who do not have automatic payments scheduled for the future. If not provided, will not filter results based on automatic payments.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/residentCenterUsers", path_params={}, query={"unitagreementids": unitagreementids, "userids": userids, "usertypes": usertypes, "residentcenteruserstatuses": residentcenteruserstatuses, "isautopayenabled": isautopayenabled, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_retail_cash_users", description="[Resident Center] Retrieve all retail cash users. Retrieves all retail cash users. Required permission(s): Rentals > Tenants - `View` OR Associations > Association owners and tenants - `View`")
    async def get_retail_cash_users(
        entityid: Annotated[int | None, Field(description="Filters results to any users associated with the specified entity id value. The value must be of the type specified in the `EntityType` field.")] = None,
        entitytype: Annotated[str | None, Field(description="Specifies the type of entity that the `EntityId` field refers to. This field is required if the `EntityId` field is provided.")] = None,
        statuses: Annotated[list[str] | None, Field(description="Filters results to any users whose lease is in one of the provided statuses.")] = None,
        name: Annotated[str | None, Field(description="Filters results to any users whose name *contains* the specified value.")] = None,
        unitaddress: Annotated[str | None, Field(description="Filters results to any users whose unit address *contains* the specified value.")] = None,
        isaccountcreated: Annotated[bool | None, Field(description="Filters results to any users whose retail cash account is created.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/retailcashusers", path_params={}, query={"entityid": entityid, "entitytype": entitytype, "statuses": statuses, "name": name, "unitaddress": unitaddress, "isaccountcreated": isaccountcreated, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_retail_cash_user", description="[Resident Center] Retrieve a retail cash user. Retrieves a retail cash user. Required permission(s): Rentals > Tenants - `View` OR Associations > Association owners and tenants - `View`")
    async def get_retail_cash_user(
        user_id: Annotated[int, Field(description="userId")],
        unit_agreement_id: Annotated[int, Field(description="unitAgreementId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/retailcashusers/{userId}/{unitAgreementId}", path_params={"userId": user_id, "unitAgreementId": unit_agreement_id}, query={}, body=None)

    @mcp.tool(name="update_retail_cash_user", description="[Resident Center] Update a retail cash user. Updates a retail cash user. Required permission(s): Rentals > Tenants - `View` `Edit` OR Associations > Association owners and tenants - `View` `Edit`")
    async def update_retail_cash_user(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        user_id: Annotated[int, Field(description="userId")],
        unit_agreement_id: Annotated[int, Field(description="unitAgreementId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/retailcashusers/{userId}/{unitAgreementId}", path_params={"userId": user_id, "unitAgreementId": unit_agreement_id}, query={}, body=body)

    @mcp.tool(name="get_task_histories", description="[Tasks] Retrieve all task history. Retrieves all task history records for a specific task. This endpoint can be used for any task type - contact requests, rental owner requests, resident requests or to do's. Required permission(s): Tasks > Tasks - `View`")
    async def get_task_histories(
        task_id: Annotated[int, Field(description="taskId")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/tasks/{taskId}/history", path_params={"taskId": task_id}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_task_history_by_id", description="[Tasks] Retrieve a task history. Retrieves a specific task history record for a task. This endpoint can be used for any task type - contact requests, rental owner requests, resident requests or to do's. Required permission(s): Tasks > Tasks - `View`")
    async def get_task_history_by_id(
        task_id: Annotated[int, Field(description="taskId")],
        task_history_id: Annotated[int, Field(description="taskHistoryId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/tasks/{taskId}/history/{taskHistoryId}", path_params={"taskId": task_id, "taskHistoryId": task_history_id}, query={}, body=None)

    @mcp.tool(name="update_task_history", description="[Tasks] Update a task history. Updates a specific task history record for a task. This endpoint can be used for any task type - contact requests, rental owner requests, resident requests or to do's. Required permission(s): Tasks > Tasks - `View` `Edit`")
    async def update_task_history(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        task_id: Annotated[int, Field(description="taskId")],
        task_history_id: Annotated[int, Field(description="taskHistoryId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/tasks/{taskId}/history/{taskHistoryId}", path_params={"taskId": task_id, "taskHistoryId": task_history_id}, query={}, body=body)

    @mcp.tool(name="get_all_task_history_files", description="[Tasks] Retrieve all task history files. Retrieves the metadata for all files associated with a task history record. This endpoint can be used for any task type - contact requests, rental owner requests, resident requests or to do's. Required permission(s): Tasks > Tasks - `View`")
    async def get_all_task_history_files(
        task_id: Annotated[int, Field(description="taskId")],
        task_history_id: Annotated[int, Field(description="taskHistoryId")],
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/tasks/{taskId}/history/{taskHistoryId}/files", path_params={"taskId": task_id, "taskHistoryId": task_history_id}, query={"orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_task_history_file_by_id", description="[Tasks] Retrieve a task history file. Retrieves the metadata for a specific file associated with a task history record. This endpoint can be used for any task type - contact requests, rental owner requests, resident requests or to do's. Required permission(s): Tasks > Tasks - `View`")
    async def get_task_history_file_by_id(
        task_id: Annotated[int, Field(description="taskId")],
        task_history_id: Annotated[int, Field(description="taskHistoryId")],
        file_id: Annotated[int, Field(description="fileId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/tasks/{taskId}/history/{taskHistoryId}/files/{fileId}", path_params={"taskId": task_id, "taskHistoryId": task_history_id, "fileId": file_id}, query={}, body=None)

    @mcp.tool(name="delete_task_history_file", description="[Tasks] Delete task history file. Deletes a specific file from a task history record. The file will be permanently deleted from the Buildium platform an can not be recovered. This endpoint can be used for any task type - contact requests, rental owner requests, resident requests or to do's. Required permission(s): Tasks > Tasks - `View` `Edit` `Delete`")
    async def delete_task_history_file(
        task_id: Annotated[int, Field(description="taskId")],
        task_history_id: Annotated[int, Field(description="taskHistoryId")],
        file_id: Annotated[int, Field(description="fileId")],
    ) -> dict[str, Any]:
        return await client.raw_request("DELETE", "/v1/tasks/{taskId}/history/{taskHistoryId}/files/{fileId}", path_params={"taskId": task_id, "taskHistoryId": task_history_id, "fileId": file_id}, query={}, body=None)

    @mcp.tool(name="create_get_file_download_request", description="[Tasks] Download a task history file. Downloads a specific file associated to the task history record. This endpoint can be used for any task type - contact requests, rental owner requests, resident requests or to do's. Required permission(s): Tasks > Tasks - `View`")
    async def create_get_file_download_request(
        task_id: Annotated[int, Field(description="taskId")],
        task_history_id: Annotated[int, Field(description="taskHistoryId")],
        file_id: Annotated[int, Field(description="fileId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/tasks/{taskId}/history/{taskHistoryId}/files/{fileId}/downloadrequest", path_params={"taskId": task_id, "taskHistoryId": task_history_id, "fileId": file_id}, query={}, body=None)

    @mcp.tool(name="create_upload_request_async_tasks", description="[Tasks] Upload a task history file. Uploads a file and associates it to the specified task history record. This endpoint can be used for any task type - contact requests, rental owner requests, resident requests or to do's. Uploading a file requires making two API requests. Each step is outlined below. Step 1 - Save file metadata The first step in the file upload process is to submit the file metadata to `/v1/tasks/{taskId}/history/{taskHistoryId}/files/uploads`. The response of this call will contain an upload URL and a collection of headers that will be used in step 2 to generate the request for the file binary upload. NOTE: The response data will expire after 5 minutes. The file metadata will not be saved in the Buildium system if step 2 of this process is not completed successfully. Step 2 - Upload the file binary Uploading the file binary will require using the response from step 1 to fo...")
    async def create_upload_request_async_tasks(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        task_id: Annotated[int, Field(description="taskId")],
        task_history_id: Annotated[int, Field(description="taskHistoryId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/tasks/{taskId}/history/{taskHistoryId}/files/uploads", path_params={"taskId": task_id, "taskHistoryId": task_history_id}, query={}, body=body)

    @mcp.tool(name="get_task_category_by_id", description="[Tasks] Retrieve a task category. Retrieves a specific task category. Required permission(s): Tasks > Tasks - `View`")
    async def get_task_category_by_id(
        task_category_id: Annotated[int, Field(description="The task category identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/tasks/categories/{taskCategoryId}", path_params={"taskCategoryId": task_category_id}, query={}, body=None)

    @mcp.tool(name="get_contact_request_tasks", description="[Contact Requests] Retrieve all contact requests. Retrieves a list of contact requests. Required permission(s): Tasks > Tasks - `View`")
    async def get_contact_request_tasks(
        entitytype: Annotated[str | None, Field(description="Specifies the type of entity that the `EntityId` field refers to. This field is required if the `EntityId` field is populated.")] = None,
        entityid: Annotated[int | None, Field(description="Filters results to any task associated with the specified entity id value. The value must be of the type specified in the `EntityType` field.")] = None,
        statuses: Annotated[list[str] | None, Field(description="Filters results by the status of the task. If no status is specified, tasks with any status will be returned.")] = None,
        unitid: Annotated[int | None, Field(description="Filters results to any task associated with the unit identifier.")] = None,
        lastupdatedfrom: Annotated[str | None, Field(description="Filters results to any tasks were updated on or after the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        lastupdatedto: Annotated[str | None, Field(description="Filters results to any tasks were updated on or before the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        duedatefrom: Annotated[str | None, Field(description="Filters results to any tasks with a due date on or after the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        duedateto: Annotated[str | None, Field(description="Filters results to any tasks with a due date on or before the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        taskcategoryid: Annotated[int | None, Field(description="Filters results to any tasks with the specified category identifier.")] = None,
        priorities: Annotated[list[str] | None, Field(description="Filters results to any tasks whose priority matches the specified values. If no priority is specified, tasks with any priority will be returned.")] = None,
        assignedtoid: Annotated[int | None, Field(description="Filters results to any tasks that have been assigned to the specified staff user identifier.")] = None,
        tasktitle: Annotated[str | None, Field(description="Filters results to any task whose title *contains* the specified value.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/tasks/contactrequests", path_params={}, query={"entitytype": entitytype, "entityid": entityid, "statuses": statuses, "unitid": unitid, "lastupdatedfrom": lastupdatedfrom, "lastupdatedto": lastupdatedto, "duedatefrom": duedatefrom, "duedateto": duedateto, "taskcategoryid": taskcategoryid, "priorities": priorities, "assignedtoid": assignedtoid, "tasktitle": tasktitle, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_contact_request_task", description="[Contact Requests] Create a contact request. Creates a contact request. Required permission(s): Tasks > Tasks - `View` `Edit`")
    async def create_contact_request_task(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/tasks/contactrequests", path_params={}, query={}, body=body)

    @mcp.tool(name="get_contact_request_task_by_id", description="[Contact Requests] Retrieve a contact request. Retrieves a contact request. Required permission(s): Tasks > Tasks - `View`")
    async def get_contact_request_task_by_id(
        contact_request_task_id: Annotated[int, Field(description="The contact request identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/tasks/contactrequests/{contactRequestTaskId}", path_params={"contactRequestTaskId": contact_request_task_id}, query={}, body=None)

    @mcp.tool(name="update_contact_request_task", description="[Contact Requests] Update a contact request. Updates a contact request. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Tasks > Tasks - `View` `Edit`")
    async def update_contact_request_task(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        contact_request_task_id: Annotated[int, Field(description="The contact request identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/tasks/contactrequests/{contactRequestTaskId}", path_params={"contactRequestTaskId": contact_request_task_id}, query={}, body=body)

    @mcp.tool(name="get_all_rental_owner_request_tasks", description="[Rental Owner Requests] Retrieve all rental owner requests. Retrieves all rental owner requests. Required permission(s): Tasks > Tasks - `View`")
    async def get_all_rental_owner_request_tasks(
        entitytype: Annotated[str | None, Field(description="Specifies the type of entity that the `EntityId` field refers to. This field is required if the `EntityId` field is populated.")] = None,
        entityid: Annotated[int | None, Field(description="Filters results to any task associated with the specified entity id value. The value must be of the type specified in the `EntityType` field.")] = None,
        statuses: Annotated[list[str] | None, Field(description="Filters results by the status of the task. If no status is specified, tasks with any status will be returned.")] = None,
        unitid: Annotated[int | None, Field(description="Filters results to any task associated with the unit identifier.")] = None,
        lastupdatedfrom: Annotated[str | None, Field(description="Filters results to any tasks were updated on or after the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        lastupdatedto: Annotated[str | None, Field(description="Filters results to any tasks were updated on or before the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        duedatefrom: Annotated[str | None, Field(description="Filters results to any tasks with a due date on or after the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        duedateto: Annotated[str | None, Field(description="Filters results to any tasks with a due date on or before the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        taskcategoryid: Annotated[int | None, Field(description="Filters results to any tasks with the specified category identifier.")] = None,
        priorities: Annotated[list[str] | None, Field(description="Filters results to any tasks whose priority matches the specified values. If no priority is specified, tasks with any priority will be returned.")] = None,
        assignedtoid: Annotated[int | None, Field(description="Filters results to any tasks that have been assigned to the specified staff user identifier.")] = None,
        tasktitle: Annotated[str | None, Field(description="Filters results to any task whose title *contains* the specified value.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/tasks/rentalownerrequests", path_params={}, query={"entitytype": entitytype, "entityid": entityid, "statuses": statuses, "unitid": unitid, "lastupdatedfrom": lastupdatedfrom, "lastupdatedto": lastupdatedto, "duedatefrom": duedatefrom, "duedateto": duedateto, "taskcategoryid": taskcategoryid, "priorities": priorities, "assignedtoid": assignedtoid, "tasktitle": tasktitle}, body=None)

    @mcp.tool(name="create_rental_owner_request_task", description="[Rental Owner Requests] Create a rental owner request. Creates a rental owner request. Required permission(s): Tasks > Tasks - `View` `Edit`")
    async def create_rental_owner_request_task(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/tasks/rentalownerrequests", path_params={}, query={}, body=body)

    @mcp.tool(name="get_rental_owner_request_task_by_id", description="[Rental Owner Requests] Retrieve a rental owner request. Retrieves a specific rental owner request. Required permission(s): Tasks > Tasks - `View`")
    async def get_rental_owner_request_task_by_id(
        rental_owner_request_task_id: Annotated[int, Field(description="The rental owner request identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/tasks/rentalownerrequests/{rentalOwnerRequestTaskId}", path_params={"rentalOwnerRequestTaskId": rental_owner_request_task_id}, query={}, body=None)

    @mcp.tool(name="update_rental_owner_request_task", description="[Rental Owner Requests] Update a rental owner request. Updates a rental owner request. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Tasks > Tasks - `View` `Edit`")
    async def update_rental_owner_request_task(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        rental_owner_request_task_id: Annotated[int, Field(description="The rental owner request identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/tasks/rentalownerrequests/{rentalOwnerRequestTaskId}", path_params={"rentalOwnerRequestTaskId": rental_owner_request_task_id}, query={}, body=body)

    @mcp.tool(name="get_rental_owner_request_task_contribution_data", description="[Rental Owner Requests] Retrieve rental owner contribution request. Retrieves the contribution details for a rental owner contribution request. Required permission(s): Tasks > Tasks - `View`")
    async def get_rental_owner_request_task_contribution_data(
        rental_owner_request_task_id: Annotated[int, Field(description="The rental owner request identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/tasks/rentalownerrequests/{rentalOwnerRequestTaskId}/contributiondata", path_params={"rentalOwnerRequestTaskId": rental_owner_request_task_id}, query={}, body=None)

    @mcp.tool(name="update_rental_owner_request_task_contribution_data", description="[Rental Owner Requests] Update a rental owner contribution request. Updates the contribution details for a rental owner contribution request. Required permission(s): Tasks > Tasks - `View` `Edit`")
    async def update_rental_owner_request_task_contribution_data(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        rental_owner_request_task_id: Annotated[int, Field(description="The rental owner request identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/tasks/rentalownerrequests/{rentalOwnerRequestTaskId}/contributiondata", path_params={"rentalOwnerRequestTaskId": rental_owner_request_task_id}, query={}, body=body)

    @mcp.tool(name="get_resident_request_tasks", description="[Resident Requests] Retrieve all resident requests. Retrieves a list of resident requests. A `unitId` of `0` indicates the resident request is not associated with a unit. Required permission(s): Tasks > Tasks - `View`")
    async def get_resident_request_tasks(
        entitytype: Annotated[str | None, Field(description="Specifies the type of entity that the `EntityId` field refers to. This field is required if the `EntityId` field is populated.")] = None,
        entityid: Annotated[int | None, Field(description="Filters results to any task associated with the specified entity id value. The value must be of the type specified in the `EntityType` field.")] = None,
        statuses: Annotated[list[str] | None, Field(description="Filters results by the status of the task. If no status is specified, tasks with any status will be returned.")] = None,
        unitid: Annotated[int | None, Field(description="Filters results to any task associated with the unit identifier.")] = None,
        unitagreementid: Annotated[int | None, Field(description="Filters results to any task associated with the unit agreement identifier specified.")] = None,
        lastupdatedfrom: Annotated[str | None, Field(description="Filters results to any tasks were updated on or after the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        lastupdatedto: Annotated[str | None, Field(description="Filters results to any tasks were updated on or before the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        duedatefrom: Annotated[str | None, Field(description="Filters results to any tasks with a due date on or after the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        duedateto: Annotated[str | None, Field(description="Filters results to any tasks with a due date on or before the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        taskcategoryid: Annotated[int | None, Field(description="Filters results to any tasks with the specified category identifier.")] = None,
        priorities: Annotated[list[str] | None, Field(description="Filters results to any tasks whose priority matches the specified values. If no priority is specified, tasks with any priority will be returned.")] = None,
        assignedtoid: Annotated[int | None, Field(description="Filters results to any tasks that have been assigned to the specified staff user identifier.")] = None,
        tasktitle: Annotated[str | None, Field(description="Filters results to any task whose title *contains* the specified value.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/tasks/residentrequests", path_params={}, query={"entitytype": entitytype, "entityid": entityid, "statuses": statuses, "unitid": unitid, "unitagreementid": unitagreementid, "lastupdatedfrom": lastupdatedfrom, "lastupdatedto": lastupdatedto, "duedatefrom": duedatefrom, "duedateto": duedateto, "taskcategoryid": taskcategoryid, "priorities": priorities, "assignedtoid": assignedtoid, "tasktitle": tasktitle, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_resource", description="[Resident Requests] Create a resident request. Creates a resident request. Required permission(s): Tasks > Tasks - `View` `Edit`")
    async def create_resource(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/tasks/residentrequests", path_params={}, query={}, body=body)

    @mcp.tool(name="get_resident_request_task", description="[Resident Requests] Retrieve a resident request. Retrieves a specific resident request. A `unitId` of `0` indicates the resident request is not associated with a unit. Required permission(s): Tasks > Tasks - `View`")
    async def get_resident_request_task(
        resident_request_task_id: Annotated[int, Field(description="The resident request identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/tasks/residentrequests/{residentRequestTaskId}", path_params={"residentRequestTaskId": resident_request_task_id}, query={}, body=None)

    @mcp.tool(name="update_resource", description="[Resident Requests] Update a resident request. Update a resident request. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Tasks > Tasks - `View` `Edit`")
    async def update_resource(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        resident_request_task_id: Annotated[int, Field(description="The resident request identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/tasks/residentrequests/{residentRequestTaskId}", path_params={"residentRequestTaskId": resident_request_task_id}, query={}, body=body)

    @mcp.tool(name="get_to_do_tasks", description="[To Do Requests] Retrieve all to do requests. Retrieves a list of to do tasks. Required permission(s): Tasks > Tasks - `View`")
    async def get_to_do_tasks(
        entitytype: Annotated[str | None, Field(description="Specifies the type of entity that the `EntityId` field refers to. This field is required if the `EntityId` field is populated.")] = None,
        entityid: Annotated[int | None, Field(description="Filters results to any task associated with the specified entity id value. The value must be of the type specified in the `EntityType` field.")] = None,
        statuses: Annotated[list[str] | None, Field(description="Filters results by the status of the task. If no status is specified, tasks with any status will be returned.")] = None,
        unitid: Annotated[int | None, Field(description="Filters results to any task associated with the unit identifier.")] = None,
        lastupdatedfrom: Annotated[str | None, Field(description="Filters results to any tasks were updated on or after the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        lastupdatedto: Annotated[str | None, Field(description="Filters results to any tasks were updated on or before the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        duedatefrom: Annotated[str | None, Field(description="Filters results to any tasks with a due date on or after the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        duedateto: Annotated[str | None, Field(description="Filters results to any tasks with a due date on or before the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        taskcategoryid: Annotated[int | None, Field(description="Filters results to any tasks with the specified category identifier.")] = None,
        priorities: Annotated[list[str] | None, Field(description="Filters results to any tasks whose priority matches the specified values. If no priority is specified, tasks with any priority will be returned.")] = None,
        assignedtoid: Annotated[int | None, Field(description="Filters results to any tasks that have been assigned to the specified staff user identifier.")] = None,
        tasktitle: Annotated[str | None, Field(description="Filters results to any task whose title *contains* the specified value.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/tasks/todorequests", path_params={}, query={"entitytype": entitytype, "entityid": entityid, "statuses": statuses, "unitid": unitid, "lastupdatedfrom": lastupdatedfrom, "lastupdatedto": lastupdatedto, "duedatefrom": duedatefrom, "duedateto": duedateto, "taskcategoryid": taskcategoryid, "priorities": priorities, "assignedtoid": assignedtoid, "tasktitle": tasktitle, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_to_do_task", description="[To Do Requests] Create a to do request. Creates a to do task. Required permission(s): Tasks > Tasks - `View` `Edit`")
    async def create_to_do_task(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/tasks/todorequests", path_params={}, query={}, body=body)

    @mcp.tool(name="get_to_do_task_by_id", description="[To Do Requests] Retrieve a to do request. Retrieves a to do task. Required permission(s): Tasks > Tasks - `View`")
    async def get_to_do_task_by_id(
        to_do_task_id: Annotated[int, Field(description="The to do task identifier")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/tasks/todorequests/{toDoTaskId}", path_params={"toDoTaskId": to_do_task_id}, query={}, body=None)

    @mcp.tool(name="update_to_do_task", description="[To Do Requests] Update a to do request. Updates a to do task NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Tasks > Tasks - `View` `Edit`")
    async def update_to_do_task(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        to_do_task_id: Annotated[int, Field(description="The to do task identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/tasks/todorequests/{toDoTaskId}", path_params={"toDoTaskId": to_do_task_id}, query={}, body=body)

    @mcp.tool(name="create_vendor_credit", description="[Vendors] Create a credit. Creates a credit. Required permission(s): Accounting > Bills - `View` `Edit`")
    async def create_vendor_credit(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        vendor_id: Annotated[int, Field(description="vendorId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/vendors/{vendorId}/credits", path_params={"vendorId": vendor_id}, query={}, body=body)

    @mcp.tool(name="get_vendor_credit", description="[Vendors] Retrieve a credit. Retrieves a credit. Required permission(s): Accounting > Bills - `View`")
    async def get_vendor_credit(
        vendor_id: Annotated[int, Field(description="vendorId")],
        vendor_credit_id: Annotated[int, Field(description="vendorCreditId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/vendors/{vendorId}/credits/{vendorCreditId}", path_params={"vendorId": vendor_id, "vendorCreditId": vendor_credit_id}, query={}, body=None)

    @mcp.tool(name="get_vendor_notes", description="[Vendors] Retrieve all notes. Retrieves all vendor notes. Required permission(s): Maintenance > Vendors - `View`")
    async def get_vendor_notes(
        vendor_id: Annotated[int, Field(description="vendorId")],
        updateddatetimefrom: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        updateddatetimeto: Annotated[str | None, Field(description="Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        lastupdatedbyuserid: Annotated[int | None, Field(description="Filters results to only notes that were last updated by the specified user identifier.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/vendors/{vendorId}/notes", path_params={"vendorId": vendor_id}, query={"updateddatetimefrom": updateddatetimefrom, "updateddatetimeto": updateddatetimeto, "lastupdatedbyuserid": lastupdatedbyuserid, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_vendor_note", description="[Vendors] Create a note. Creates a vendor note. Required permission(s): Maintenance > Vendors - `View` `Edit`")
    async def create_vendor_note(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        vendor_id: Annotated[int, Field(description="vendorId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/vendors/{vendorId}/notes", path_params={"vendorId": vendor_id}, query={}, body=body)

    @mcp.tool(name="get_vendor_note_by_note_id", description="[Vendors] Retrieve a note. Retrieves a vendor note. Required permission(s): Maintenance > Vendors - `View`")
    async def get_vendor_note_by_note_id(
        vendor_id: Annotated[int, Field(description="vendorId")],
        note_id: Annotated[int, Field(description="noteId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/vendors/{vendorId}/notes/{noteId}", path_params={"vendorId": vendor_id, "noteId": note_id}, query={}, body=None)

    @mcp.tool(name="update_vendor_note", description="[Vendors] Update a note. Updates a vendor note. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Maintenance > Vendors - `View` `Edit`")
    async def update_vendor_note(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        vendor_id: Annotated[int, Field(description="vendorId")],
        note_id: Annotated[int, Field(description="noteId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/vendors/{vendorId}/notes/{noteId}", path_params={"vendorId": vendor_id, "noteId": note_id}, query={}, body=body)

    @mcp.tool(name="create_vendor_refund", description="[Vendors] Create a refund. Creates a refund. Required permission(s): Maintenance > Vendors - `View` `Edit` Accounting > Bank Accounts - `View`")
    async def create_vendor_refund(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        vendor_id: Annotated[int, Field(description="vendorId")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/vendors/{vendorId}/refunds", path_params={"vendorId": vendor_id}, query={}, body=body)

    @mcp.tool(name="get_vendor_refund", description="[Vendors] Retrieve a refund. Retrieves a refund. Required permission(s): Maintenance > Vendors - `View`")
    async def get_vendor_refund(
        vendor_id: Annotated[int, Field(description="vendorId")],
        vendor_refund_id: Annotated[int, Field(description="vendorRefundId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/vendors/{vendorId}/refunds/{vendorRefundId}", path_params={"vendorId": vendor_id, "vendorRefundId": vendor_refund_id}, query={}, body=None)

    @mcp.tool(name="get_all_vendor_transactions", description="[Vendors] Retrieve all transactions. Retrieves all transactions for a given vendor. Required permission(s): Maintenance > Vendors - `View` Accounting > General Ledger Transactions - `View`")
    async def get_all_vendor_transactions(
        transactiondatefrom: Annotated[str, Field(description="Filters results to any vendor transaction whose entry date that is greater than or equal to the specified value. The maximum date range is 365 days.")],
        transactiondateto: Annotated[str, Field(description="Filters results to any vendor transaction whose entry date is less than or equal to the specified value. The maximum date range is 365 days.")],
        vendor_id: Annotated[int, Field(description="vendorId")],
        transactiontypes: Annotated[list[str] | None, Field(description="Filters results to any vendor transaction whose vendor transaction type matches the specified status. If no type is specified, vendor transactions with any type will be returned.")] = None,
        referencenumber: Annotated[str | None, Field(description="Filters results to vendor transaction whose reference number contains the specified value. The reference number cannot exceed 40 characters.")] = None,
        memo: Annotated[str | None, Field(description="Filters results to vendor transaction whose memo contains the specified value. The memo cannot exceed 40 characters.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/vendors/{vendorId}/transactions", path_params={"vendorId": vendor_id}, query={"transactiondatefrom": transactiondatefrom, "transactiondateto": transactiondateto, "transactiontypes": transactiontypes, "referencenumber": referencenumber, "memo": memo, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="get_vendor_category_by_id", description="[Vendors] Retrieve a vendor category. Retrieves a specific vendor category. Required permission(s): Maintenance > Vendors - `View`")
    async def get_vendor_category_by_id(
        vendor_category_id: Annotated[int, Field(description="The vendor category identifier.")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/vendors/categories/{vendorCategoryId}", path_params={"vendorCategoryId": vendor_category_id}, query={}, body=None)

    @mcp.tool(name="get_all_work_orders", description="[Work Orders] Retrieve all work orders. Retrieves a list of work orders. Required permission(s): Maintenance > Work Orders - `View`")
    async def get_all_work_orders(
        entitytype: Annotated[str | None, Field(description="Specifies the type of entity that the `EntityId` field refers to. This field is required if the `EntityId` field is populated.")] = None,
        entityid: Annotated[int | None, Field(description="Filters results to any work order associated with the specified entity id value. The value must be of the type specified in the `EntityType` field.")] = None,
        statuses: Annotated[list[str] | None, Field(description="Filters results by the status of the task associated with the work order. If no status is specified, work orders with any status will be returned.")] = None,
        type: Annotated[str | None, Field(description="Filters results to any work order with an associated task with the task type specified.")] = None,
        unitid: Annotated[int | None, Field(description="Filters results to any work order associated with the unit identifier.")] = None,
        unitagreementid: Annotated[int | None, Field(description="Filters results to any work order associated with the unit agreement identifier specified.")] = None,
        lastupdatedfrom: Annotated[str | None, Field(description="Filters results to any work orders were updated on or after the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        lastupdatedto: Annotated[str | None, Field(description="Filters results to any work orders were updated on or before the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        duedatefrom: Annotated[str | None, Field(description="Filters results to any work orders with a due date on or after the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        duedateto: Annotated[str | None, Field(description="Filters results to any work orders with a due date on or before the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        taskcategoryid: Annotated[int | None, Field(description="Filters results to any work orders with the specified task category identifier.")] = None,
        priorities: Annotated[list[str] | None, Field(description="Filters results to any work orders whose priority matches the specified values. If no priority is specified, tasks with any priority will be returned.")] = None,
        assignedtoid: Annotated[int | None, Field(description="Filters results to any work orders that have been assigned to the specified staff user identifier.")] = None,
        vendorids: Annotated[list[int] | None, Field(description="Filters results to any work orders that have been assigned to the specified vendor identifier.")] = None,
        amountfrom: Annotated[float | None, Field(description="Filters results to any work orders whose total amounts are equal or greater than the specified amount.")] = None,
        amountto: Annotated[float | None, Field(description="Filters results to any work orders whose total amounts are equal or less than the specified amount.")] = None,
        isbilled: Annotated[bool | None, Field(description="Filters results to work orders that have an associated bill.")] = None,
        title: Annotated[str | None, Field(description="Filters results to any work orders whose title *contains* the specified value.")] = None,
        taskids: Annotated[list[int] | None, Field(description="Filters results to work orders that have an associated to a task in the specified list.")] = None,
        orderby: Annotated[str | None, Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See Bulk Request Options for more information.")] = None,
        offset: Annotated[int | None, Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[int | None, Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/workorders", path_params={}, query={"entitytype": entitytype, "entityid": entityid, "statuses": statuses, "type": type, "unitid": unitid, "unitagreementid": unitagreementid, "lastupdatedfrom": lastupdatedfrom, "lastupdatedto": lastupdatedto, "duedatefrom": duedatefrom, "duedateto": duedateto, "taskcategoryid": taskcategoryid, "priorities": priorities, "assignedtoid": assignedtoid, "vendorids": vendorids, "amountfrom": amountfrom, "amountto": amountto, "isbilled": isbilled, "title": title, "taskids": taskids, "orderby": orderby, "offset": offset, "limit": limit}, body=None)

    @mcp.tool(name="create_work_order", description="[Work Orders] Create a work order. Creates a work order. Required permission(s): Maintenance > Work Orders - `View` `Edit`")
    async def create_work_order(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
    ) -> dict[str, Any]:
        return await client.raw_request("POST", "/v1/workorders", path_params={}, query={}, body=body)

    @mcp.tool(name="get_work_order_by_id", description="[Work Orders] Retrieve a work order. Retrieves a specific work order. Required permission(s): Maintenance > Work Orders - `View`")
    async def get_work_order_by_id(
        work_order_id: Annotated[int, Field(description="workOrderId")],
    ) -> dict[str, Any]:
        return await client.raw_request("GET", "/v1/workorders/{workOrderId}", path_params={"workOrderId": work_order_id}, query={}, body=None)

    @mcp.tool(name="update_work_order", description="[Work Orders] Update a work order. Updates a work order. NOTE: Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated. Required permission(s): Maintenance > Work Orders - `View` `Edit`")
    async def update_work_order(
        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],
        work_order_id: Annotated[int, Field(description="workOrderId")],
    ) -> dict[str, Any]:
        return await client.raw_request("PUT", "/v1/workorders/{workOrderId}", path_params={"workOrderId": work_order_id}, query={}, body=body)

