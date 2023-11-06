records = {
    "cricket": [
        {
            "batting_records": [
                {
                    "test_records": [
                        {
                            "most_runs": [
                                {
                                    "sachin": 15000
                                },
                                {
                                    "sangkara": 14000
                                },
                                {
                                    "Kallis": 13500
                                }
                            ]
                        },
                        {
                            "most_centuaries": [
                                {
                                    "sachin": 51
                                },
                                {
                                    "sangkara": 37
                                },
                                {
                                    "Kallis": 43
                                }
                            ]
                        }
                    ]
                },
                {
                    "odi_records": [
                        {
                            "most_runs": [
                                {
                                    "sachin": 18500
                                },
                                {
                                    "sangkara": 14200
                                },
                                {
                                    "Ponting": 13700
                                },
                                {
                                    "Kohli": 13400
                                }
                            ]
                        },
                        {
                            "most_centuaries": [
                                {
                                    "sachin": 49
                                },
                                {
                                    "kohli": 48
                                },
                                {
                                    "Rhoit": 31
                                },
                                {
                                    "Ponting": 30
                                }
                            ]
                        }
                    ]
                },
                {
                    "t20_records": [
                        {
                            "most_runs": [
                                {
                                    "kohli": 4000
                                },
                                {
                                    "Rohit": 3900
                                },
                                {
                                    "Warner": 3500
                                }
                            ]
                        },
                        {
                            "most_centuaries": [
                                {
                                    "Rohit": 3
                                },
                                {
                                    "kohli": 2
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "bowling_records": [
                {
                    "test_records": [
                        {
                            "most_wickets": [
                                {
                                    "murlidharan": 800
                                },
                                {
                                    "warne": 750
                                },
                                {
                                    "anderson": 690
                                }
                            ]
                        }
                    ]
                },
                {
                    "odi_records": [
                        {
                            "most_wickets": [
                                {
                                    "murlidharan": 550
                                },
                                {
                                    "wasimakram": 500
                                },
                                {
                                    "anderson": 450
                                }
                            ]
                        }
                    ]
                },
                {
                    "t20_records": [
                        {
                            "most_wickets": [
                                {
                                    "Ashwin": 150
                                },
                                {
                                    "Bumrah": 140
                                },
                                {
                                    "Shami": 120
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}

#print(type(records))
#print(records.get("cricket")[0].get("batting_records")[1])


#print(records.get("cricket")[1].get("bowling_records")[0].get("test_records")[0].get("most_wickets")[1])

sum=0 
for rec in records.get("cricket")[0].get("batting_records")[0].get("test_records")[0].get("most_runs"):
    for runs in rec.values():
        sum+=runs

print(sum)    