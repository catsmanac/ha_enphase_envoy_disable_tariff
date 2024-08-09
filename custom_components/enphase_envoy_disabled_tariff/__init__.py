"""Initialization for Enphase Envoy disabled Tariff.

This custom integration removes the EnvoyTariffUpdater from the Pyenphase module used
by the HA Core Enphase Envoy integration. When registered, the HA Enphase Envoy
no longer collect /admin/lib/tariff endpoint.
"""
from __future__ import annotations

import logging

from pyenphase import register_updater
from pyenphase.envoy import get_updaters
from pyenphase.updaters.base import EnvoyUpdater
from pyenphase.updaters.tariff import EnvoyTariffUpdater

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv

from .const import DOMAIN

# Use empty_config_schema because the component does not have any config options
CONFIG_SCHEMA = cv.empty_config_schema(DOMAIN)

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: ConfigEntry):
    """Remove the EnvoyTariffUpdater Pyenphase UPDATERS."""
    updaters: list[type[EnvoyUpdater]] = get_updaters()
    if EnvoyTariffUpdater  in updaters:
        if _LOGGER.level == logging.DEBUG:
            _LOGGER.debug("Removing EnvoyTariffUpdater from Pyenphase")
        updaters.remove(EnvoyTariffUpdater)
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Enphase Envoy disabled tariff from a config entry."""
    return True
