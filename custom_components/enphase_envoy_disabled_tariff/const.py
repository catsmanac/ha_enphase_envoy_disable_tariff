"""Initialization for Enphase Envoy disabled Tariff.

This custom integration removes the EnvoyTariffUpdater from the Pyenphase module used
by the HA Core Enphase Envoy integration. When registered, the HA Enphase Envoy
no longer collect /admin/lib/tariff endpoint.
"""
DOMAIN = "enphase_envoy_disabled_tariff"

CONF_UPDATER = "updater"

NAME = "Enphase Envoy disabled Tariff"

UNIQUE_ID = f"{DOMAIN}_for_enphase_envoy"
