Feature: Library Information System API test

  Scenario Outline: Retrieves the list of Author
     Given the endpoint author
     And param <parameters>
     When method get
     Then the response status is <response_status>
     And the response matches <response_schema> schema
    Examples:
       |  parameters  | response_status    | response_schema             |
       |  default     |    200             | authorlist-schema.json      |
       |  not_existed |    400             | bad-request-schema.json     |
