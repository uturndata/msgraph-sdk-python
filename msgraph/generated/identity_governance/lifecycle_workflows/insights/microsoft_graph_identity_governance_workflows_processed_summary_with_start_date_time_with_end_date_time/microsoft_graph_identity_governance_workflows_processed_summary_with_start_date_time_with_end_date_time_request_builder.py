from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from .....models.identity_governance.workflows_insights_summary import WorkflowsInsightsSummary
    from .....models.o_data_errors.o_data_error import ODataError

class MicrosoftGraphIdentityGovernanceWorkflowsProcessedSummaryWithStartDateTimeWithEndDateTimeRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the workflowsProcessedSummary method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]], end_date_time: Optional[datetime.datetime] = None, start_date_time: Optional[datetime.datetime] = None) -> None:
        """
        Instantiates a new MicrosoftGraphIdentityGovernanceWorkflowsProcessedSummaryWithStartDateTimeWithEndDateTimeRequestBuilder and sets the default values.
        param end_date_time: Usage: endDateTime={endDateTime}
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        param start_date_time: Usage: startDateTime={startDateTime}
        Returns: None
        """
        if isinstance(path_parameters, dict):
            path_parameters['endDateTime'] = end_date_time
            path_parameters['startDateTime'] = start_date_time
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/lifecycleWorkflows/insights/microsoft.graph.identityGovernance.workflowsProcessedSummary(startDateTime={startDateTime},endDateTime={endDateTime})", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WorkflowsInsightsSummary]:
        """
        Provide a summary of all workflows processed within a tenant for a specified period. Because the amount of results for listed workflows as returned by the List workflows does not tell you which workflows were processed from the list of created workflows, this summary gives you a quick overview of processed status based on counts.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WorkflowsInsightsSummary]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.identity_governance.workflows_insights_summary import WorkflowsInsightsSummary

        return await self.request_adapter.send_async(request_info, WorkflowsInsightsSummary, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Provide a summary of all workflows processed within a tenant for a specified period. Because the amount of results for listed workflows as returned by the List workflows does not tell you which workflows were processed from the list of created workflows, this summary gives you a quick overview of processed status based on counts.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> MicrosoftGraphIdentityGovernanceWorkflowsProcessedSummaryWithStartDateTimeWithEndDateTimeRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MicrosoftGraphIdentityGovernanceWorkflowsProcessedSummaryWithStartDateTimeWithEndDateTimeRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MicrosoftGraphIdentityGovernanceWorkflowsProcessedSummaryWithStartDateTimeWithEndDateTimeRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class MicrosoftGraphIdentityGovernanceWorkflowsProcessedSummaryWithStartDateTimeWithEndDateTimeRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

