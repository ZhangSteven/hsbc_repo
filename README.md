# hsbc_repo

Convert HSBC Repo holdings file to csv format for Geneva reconciliation purpose.

Output csv file will have the following columns (similar to citi package),

For position csv:

portfolio|custodian|date|geneva_investment_id|ISIN|bloomberg_figi|name|currency|quantity


For cash csv:

portfolio|custodian|date|currency|balance