// Map-specific tracking
function trackMapInteractions() {
    // Track map viewport changes
    if (typeof map !== 'undefined') {
        map.on('moveend', function () {
            const center = map.getCenter();
            gtag('event', 'map_pan', {
                'event_category': 'map_interaction',
                'event_label': 'viewport_change',
                'value': 1,
                'latitude': center.lat,
                'longitude': center.lng,
                'zoom': map.getZoom()
            });
        });

        // Track zoom level changes
        map.on('zoomend', function () {
            gtag('event', 'map_zoom', {
                'event_category': 'map_interaction',
                'event_label': 'zoom_change',
                'value': map.getZoom()
            });
        });
    }

    // Track map layer toggles if you have any
    document.querySelectorAll('.map-layer-toggle').forEach(toggle => {
        toggle.addEventListener('change', function () {
            gtag('event', 'layer_toggle', {
                'event_category': 'map_interaction',
                'event_label': this.id,
                'value': this.checked ? 1 : 0
            });
        });
    });
}

// Initialize tracking when the page loads
document.addEventListener('DOMContentLoaded', trackMapInteractions); 