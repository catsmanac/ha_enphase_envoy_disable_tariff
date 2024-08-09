"""Initialization for Enphase Envoy disabled Tariff.

This custom integration removes the EnvoyTariffUpdater from the Pyenphase module used
by the HA Core Enphase Envoy integration. When registered, the HA Enphase Envoy
no longer collect /admin/lib/tariff endpoint.
"""
import logging
from typing import Any

from homeassistant import config_entries

from .const import CONF_UPDATER, DOMAIN, NAME, UNIQUE_ID

_LOGGER = logging.getLogger(__name__)


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Enphase Envoy disabled Tariff config flow."""

    VERSION = 1

    async def async_step_user(self, user_input: dict[str, Any] | None = None):
        if not self.unique_id:
            await self.async_set_unique_id(UNIQUE_ID)
        if self.unique_id:
            self._abort_if_unique_id_configured(error="single_instance_allowed")
        return self.async_create_entry(
            title=NAME,
            data={CONF_UPDATER: "Enphase_Envoy_disable_tariff_updater"}
        )
