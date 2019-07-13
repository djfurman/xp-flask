Feature: Discoverable API

   As a developer,
   when I use the API;
   then I want to be able to navigate it
   without having to fully read the documents

    @api @v1
    Scenario: API Versions
        When a GET request to "/api"
        Then the response status code should be "200"
        And the response header "content-type" should be "application/json"
        And the json response body should show "v1"
