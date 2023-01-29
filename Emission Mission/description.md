# Challenge description

Part of BAE Systems Digital Intelligence's climate change strategy is developing renewable energy sources on-site. Your job is to forecast 24 hours of energy usage and calculate the associated carbon emissions.

You are provided with a list of projects and a renewable energy forecast. The renewable energy can be assumed to produce no emissions, however if there is not sufficient renewable energy to meet demand then grid electricity will have to be used, which has an associated emission output of 1 arbitrary unit per unit of electricity.

The renewable energy forecast is provided as a list of 24 non-negative integers, which is the associated renewable energy produced each hour from midnight(00). Finally, the projects are strings in the `format[time ranges];[energy]` where energy is the non-negative hourly energy consumption and time ranges are the operating hours of said project. The time ranges will be comma-seperated and either in the form `A-B #0 <= A < B <= 24` or `A` which is as before with `B=A+1` implicitly (note that the range excludes B i.e. 1-2 is only one hour long). A and B will be 0 padded if necessary however overlaps in time ranges are possible and should be discounted.

Calculate the total emissions over the 24 hour period, which will be an integer.