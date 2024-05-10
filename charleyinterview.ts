const axios = require('axios');
import * as _ from 'lodash'

// slow async external API
// list of cities 
// given a city, get current weather

// get weather frequently, every hour? could be more frequent later on
// maximum team size up to 50 people, but will be larger teams later on
// want it to be pretty quick, start simple but optimize later  


// what happens if list is 100 long?
// use worker queue that keeps trying to get the data, pops from the queue when done with one
// 2 figure out how to do worker queues with javascript
// 3 now that you have this system, how would you scale it up to handle millions of requests per...hour?
// only want to make hundreds of thousands of API requests, use cache
// cache for location data (no expiration), cache for weather data (with TTL)
type CityWeatherData = {
  cityName: string
  weather: Weather
}

type Weather = {
  temp: number
}

type CityLocationData = {
  cityName: string
  location: Coordinates
}

type Coordinates = {
  latitude: number
  longitude: number
}

async function getCityData(str: string): Promise<CityLocationData | undefined> {
  const encoded = encodeURI(str)
  try { 
    const response = await axios.get(`http://api.openweathermap.org/geo/1.0/direct?q=${encoded}&limit=5&appid=34f0f55e04320b79c50d361c3cd2a115`);

    if (response['data'] && Array.isArray(response['data']) && response['data'].length > 0) {
      const firstResult = response['data'][0]
      if (firstResult['lat'] && firstResult['lon']) {
        return {
          cityName: str, 
          location: {
            latitude: firstResult['lat'],
            longitude: firstResult['lon']
          }
        }
      }
    }
    else {
      console.warn(`Location not found for ${str}`)
      console.log(response)
    }
    return undefined
  } catch (error) {
    console.error(error);
    return undefined
  }
}

async function getWeather(lat: number, lon: number): Promise<Weather | undefined> {
  try { 
    const response = await axios.get(`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=34f0f55e04320b79c50d361c3cd2a115`);

    if (response['data'] && response['data']['main'] && response['data']['main']['temp'] && typeof response['data']['main']['temp'] === 'number') {
      return { temp: response['data']['main']['temp'] - 273.15 }
    }
    return undefined
  } catch (error) {
    console.error(error);
    return undefined
  }
}

async function main() {
  const cities = [
    "London",
    "Paris",
    "San Francisco, CA, US",
    "New York, NY, US",
    "Alameda, CA",
    "Montevideo",
    "Aarhus",
    "Victoria, BC, Canada",
    "Vancouver, BC, Canada",
    "Sacramento, CA, US",
    "Las Vegas, NV, US",
    "Portland, OR, US"
    ]

    // input is array of city strings, output is structured weather data 
    // define API first, make a function, main should call that function with example test cases
  
  const citiesData = await Promise.all(cities.map(async (city: string) => {
    return getCityData(city)
  } ))

  const compactCitiesData: CityLocationData[] = _.compact(citiesData)

  console.log(compactCitiesData)

  const citiesWeatherData = await Promise.all(compactCitiesData.map(async (cityData: CityLocationData) => {
    const weather = await getWeather(cityData.location.latitude, cityData.location.longitude)
    if (weather) {
      const result: CityWeatherData = {
        cityName: cityData.cityName,
        weather: weather
      }
      return result
    }
    return undefined
  }))

  const compactWeather = _.compact(citiesWeatherData)

  console.log(compactWeather)
}

main()


