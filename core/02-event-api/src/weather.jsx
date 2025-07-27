{"Application Programming Interface (API) helper for fetching weather data"}

const API_KEY = import.meta.env.VITE_WEATHER_API_KEY;

export async function fetchWeather() {
  const lat = 51.5074;  // London's latitude
  const lon = -0.1278;  // London's longitude
  const units = "metric";

  const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=${units}&appid=${API_KEY}`;

  {"'fetch request' weather data from OpenWeatherMap API"}
  const res = await fetch(url);
  if (!res.ok) throw new Error("Failed to fetch weather");
  return await res.json();
}
