"""Initialization for Enphase Envoy disabled Tariff.

This custom integration removes the EnvoyTariffUpdater from the Pyenphase module used
by the HA Core Enphase Envoy integration. When registered, the HA Enphase Envoy
no longer collect /admin/lib/tariff endpoint.
"""
from __future__ import annotations

from typing import Any

from attr import asdict

from homeassistant.config_entries import ConfigEntry

from pyenphase.envoy import get_updaters
from pyenphase.updaters.base import EnvoyUpdater
from pyenphase.updaters.tariff import EnvoyTariffUpdater

async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""

    updaters: list[type[EnvoyUpdater]] = get_updaters()
    tariff_disabled = (EnvoyTariffUpdater not in updaters)


    diagnostic_data: dict[str, Any] = {
        "config_entry": entry.as_dict(),
        "Disabled_tariff": tariff_disabled,
    }

    return diagnostic_data
