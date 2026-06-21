-- Total records
SELECT COUNT(*) AS total_records
FROM covid_data;

-- Top 10 countries by confirmed cases
SELECT Country_Region,
       MAX(Confirmed) AS Total_Confirmed
FROM covid_data
GROUP BY Country_Region
ORDER BY Total_Confirmed DESC
LIMIT 10;

-- Top 10 countries by deaths
SELECT Country_Region,
       MAX(Deaths) AS Total_Deaths
FROM covid_data
GROUP BY Country_Region
ORDER BY Total_Deaths DESC
LIMIT 10;

-- Top 10 countries by recoveries
SELECT Country_Region,
       MAX(Recovered) AS Total_Recovered
FROM covid_data
GROUP BY Country_Region
ORDER BY Total_Recovered DESC
LIMIT 10;