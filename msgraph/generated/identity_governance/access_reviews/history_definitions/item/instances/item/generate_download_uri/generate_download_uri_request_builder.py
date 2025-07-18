from __future__ import annotations
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
    from ........models.access_review_history_instance import AccessReviewHistoryInstance
    from ........models.o_data_errors.o_data_error import ODataError

class GenerateDownloadUriRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the generateDownloadUri method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new GenerateDownloadUriRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/accessReviews/historyDefinitions/{accessReviewHistoryDefinition%2Did}/instances/{accessReviewHistoryInstance%2Did}/generateDownloadUri", path_parameters)
    
    async def post(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AccessReviewHistoryInstance]:
        """
        Generates a URI for an accessReviewHistoryInstance object the status for which is done. Each URI can be used to retrieve the instance's review history data. Each URI is valid for 24 hours and can be retrieved by fetching the downloadUri property from the accessReviewHistoryInstance object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessReviewHistoryInstance]
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.access_review_history_instance import AccessReviewHistoryInstance

        return await self.request_adapter.send_async(request_info, AccessReviewHistoryInstance, error_mapping)
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Generates a URI for an accessReviewHistoryInstance object the status for which is done. Each URI can be used to retrieve the instance's review history data. Each URI is valid for 24 hours and can be retrieved by fetching the downloadUri property from the accessReviewHistoryInstance object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> GenerateDownloadUriRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: GenerateDownloadUriRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return GenerateDownloadUriRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class GenerateDownloadUriRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

