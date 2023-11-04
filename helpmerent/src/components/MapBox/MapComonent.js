import React, {useRef, useState, useEffect } from 'react';
import "mapbox-gl/dist/mapbox-gl.css";
import mapboxgl from 'mapbox-gl';

import Map, {
    Marker,
    NavigationControl,
    Popup,
    FullscreenControl,
    GeolocateControl,
  } from "react-map-gl";

const MAPBOX_TOKEN = 'pk.eyJ1IjoiYXhrNjcwIiwiYSI6ImNsbjVka2l5cTA2NTcycHF1MnFoNHh5bzgifQ.cSIgT6DWblr6rZMBPU4BWQ'; // Replace with your Mapbox Access Token


function MapComponent() {
    const mapContainer = useRef(null);
    const [lng, setLng] = useState(151.22);
    const [lat, setLat] = useState(-33.91);
    const [zoom, setZoom] = useState(13);
  
    useEffect(() => {
      mapboxgl.accessToken = MAPBOX_TOKEN; 
  
      const map = new mapboxgl.Map({
        container: mapContainer.current,
        style: 'mapbox://styles/mapbox/streets-v12',
        center: [lng, lat],
        zoom: zoom,
      });
  
      return () => map.remove();
    }, [lng, lat, zoom]);

    return (
      <div>
        <div ref={mapContainer} className="map-container" style={{ width: '100%', height: '700px' }} />
      </div>
    );
  }
export default MapComponent;