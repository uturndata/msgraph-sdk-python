from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .location import Location

@dataclass
class EmergencyCallerInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The displayName property
    display_name: Optional[str] = None
    # The location property
    location: Optional[Location] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The phoneNumber property
    phone_number: Optional[str] = None
    # The tenantId property
    tenant_id: Optional[str] = None
    # The upn property
    upn: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EmergencyCallerInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EmergencyCallerInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EmergencyCallerInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .location import Location

        from .location import Location

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(Location)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "upn": lambda n : setattr(self, 'upn', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("location", self.location)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("upn", self.upn)
        writer.write_additional_data_value(self.additional_data)
    

