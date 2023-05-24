# Overview
In this assignment, I chose to continue working with the same Divvy bike trip data
as Assignments 7 and 8. I was curious if I could work with spatial data tools
in Python to visualize the large-scale trip data from Q3 2018, and if visualization
would reveal any interesting patterns.

# Takeaways
Based on my visualization, I argue that there was tentative evidence for geographic inequality in Divvy usage in Chicago as of Q3 2018. This inequality seemed to persist even though I normalized trip counts per station by the bikes available at that station. There was high bike usage on the North Side, but that usage drastically dropped off moving to the South, West, and Southwest Sides (with the notable exception of Hyde Park, due to the presence of the University of Chicago).

There were also noticeably fewer bike stations in communities like North/South Lawndale (on the West Side) and Englewood (on the South Side), compared to equivalently-sized or smaller community areas on the North Side like Lincoln Park, Lakeview, and even Edgewater and Rogers Park. In Q3 2018, some core communities in the Southwest Side (e.g, Gage Park) did not have Divvy stations at all. Divvy did not reach these communities until a [2020 expansion](https://ride.divvybikes.com/explore-chicago/expansion).

It's easy to see the north-south inequality simply by tracing the line of yellow dots (high bike usage) that turn purple (low bike usage) on a major north-south street: Halsted, for example.

A caveat is that beyond the number of total docks available at a station, my analysis doesn't control for additional differences between bike stations/community areas. For instance, I don't control for the population density of the community area surrounding the origin station, level of economic activity around the station, or distance to the nearest station. All these are factors should be highly correlated with number of trips taken from a Divvy station. Since I'm not able to account for them, I can't fully capture the association between geographical area and bike usage.

# Explanation and Policy Implications

From my own observation around Chicago, leisure and commuting seem to be the two primary motivations behind taking a Divvy. It's an interesting exercise to use microeconomic theory to model why some stations see less activity than others. For instance, we might denote individuals who seek to use Divvy for leisure as type $L$, while denoting commuters as type $C$. Each type has different preferences over trip length and cost, the two factors I assume that matter the most in choosing transportation. Each type of person has access to Divvy and outside transportation option(s) such as taking the bus or driving.

Divvy operates on a pay-per-ride or yearly subscription scheme. Both of these payment methods might be too high of a cost for a resident on the South Side but easily affordable for a resident on the North Side, which might partially explain why more trips are taken on the North Side. Furthermore, the North Side might have more type $L$ individuals who ride bikes only on the North Side, as many Chicago tourist attractions like Lincoln Park are located there. This also explains higher trip activity on the North Side.

The policy implications of this and my visualization, however, are unclear. It's likely that there is bike inequality in Chicago, and combating it would likely diminish transportation inequality. However, the city should do more research into why inequality in bike usage exists before launching a specific policy. Is it because the South Side simply has fewer Divvy stations compared to the North Side; because Divvy's pricing is too expensive; because South Side residents might find taking the bus or driving more convenient; or all of the above? Chicago should spend the resources and time to investigate the answers to these questions. Doing so will leave the city with a better understanding of the feasibility and goals of any policy to combat bike inequality and transportation inequality in general.

# Technical Description
I used PySpark to wrangle the raw data, and sent the result to `geopandas`
for additional spatial data wrangling and visualization. To create
the gif, I first wrote a `for` loop to repeatedly plot each still frame.
Finally, I used `flask` to host a local web app to present the results. Below
is a screenshot of the app running on my local server.

![](https://github.com/macs30113-s23/a9-bryantco/blob/main/images/screenshot_flask.PNG)
