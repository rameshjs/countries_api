# COUNTRY DATA PROVIDER 🇮🇳
Get information on any country, from population and languages to currencies and more via restful api.

# ABOUT THIS PROJECT
This open-source project draws inspiration from restcountries.eu and restcountries.com. While the original project has transitioned to a subscription-based API, and the second project lacks a robust filtering or structured means of querying country data, I am actively addressing these issues with the aim of enhancing the accessibility and usability of this project.

# COUNTRY DATA  
You can access the API via `http://localhost:8000/api/v1/{endpoint}`

# ENDPOINTS

## ALL COUNTRIES DATA
To retrieve data for all countries, you can use the following link: 
`http://localhost:8000/api/v1/countries/all`

## FILTER COUNTRY DATA

### Available filter queries

| Field | Filter query |
| --- | ------------------- |
| common_name | ?common_name__icontains={value} |
| official_name | ?official_name__icontains={value} |
| cca2 | ?cca2__iexact={value} |
| ccn3 | ?ccn3__iexact={value} |
| cca3 | ?cca3__iexact={value} |
| cioc | ?cioc__iexact={value} |
| currencies__name | ?currencies__name__iexact={value} |
| currencies__name | ?currencies__name__icontains={value} |
| currencies__code | ?currencies__code__iexact={value} |
| currencies__code | ?currencies__code__icontains={value} |

### Example
`http://localhost:8000/api/v1/countries/all?common_name__icontains={value}`








