import pandas as pd

# Sample data for retirement plans
data = [
    ["RetireWell 401(k)", "Tax-deferred contributions", "₹50,000 per annum", "Age 18-60 years", "retirewell@example.com", "1800-123-4567"],
    ["GoldenYears Pension Plan", "Lifetime income option", "₹1,00,000 lump sum", "Age 25-55 years", "goldenyears@example.com", "1800-987-6543"],
    ["SecureRetire Annuity", "Guaranteed returns", "₹25,000 per annum", "Age 30-65 years", "secureretire@example.com", "1800-567-8901"],
    ["FutureNest Retirement Fund", "Flexible investment options", "₹10,000 monthly SIP", "Age 22-58 years", "futurenest@example.com", "1800-234-5678"],
    ["PensionPlus Savings Scheme", "Tax benefits under Section 80C", "₹5,000 per month", "Age 20-50 years", "pensionplus@example.com", "1800-345-6789"],
    ["WealthRetire Plan", "Investment diversification", "₹75,000 per annum", "Age 28-60 years", "wealthretire@example.com", "1800-876-5432"],
    ["SmartSaver Pension Scheme", "Auto-adjusting portfolio", "₹20,000 quarterly", "Age 25-55 years", "smartsaver@example.com", "1800-345-6780"],
    ["GoldenSun Retirement Annuity", "Life cover option", "₹1,50,000 lump sum", "Age 35-65 years", "goldensun@example.com", "1800-789-0123"],
    ["FlexiSecure Retirement Fund", "Partial withdrawal allowed", "₹15,000 monthly SIP", "Age 30-55 years", "flexisecure@example.com", "1800-234-5670"],
    ["EduPension Plan", "Education benefit for children", "₹8,000 per month", "Age 25-50 years", "edupension@example.com", "1800-456-7890"],
    ["DreamRetire Life Annuity", "Customizable maturity age", "₹50,000 annually", "Age 20-60 years", "dreamretire@example.com", "1800-890-1234"],
    ["SecureNest Retirement Scheme", "Tax-free withdrawals", "₹30,000 per annum", "Age 30-65 years", "securenest@example.com", "1800-567-8901"],
    ["FreedomPension Fund", "Flexible contribution options", "₹12,000 monthly SIP", "Age 22-58 years", "freedomfund@example.com", "1800-234-5678"],
    ["EcoSaver Retirement Plan", "Sustainable investment options", "₹40,000 per annum", "Age 25-55 years", "ecosaver@example.com", "1800-345-6789"],
    ["SunriseRetire Annuity", "Guaranteed income for life", "₹2,00,000 lump sum", "Age 35-70 years", "sunriseretire@example.com", "1800-789-0123"],
    ["WiseChoice Pension Scheme", "Smart investment advisory", "₹25,000 quarterly", "Age 28-60 years", "wisechoice@example.com", "1800-876-5432"],
    ["GoldenNest Retirement Fund", "High growth potential", "₹18,000 monthly SIP", "Age 30-65 years", "goldennest@example.com", "1800-345-6780"],
    ["SecureLife Pension Plan", "Life cover with monthly payout", "₹1,20,000 lump sum", "Age 25-55 years", "securelife@example.com", "1800-789-0123"],
    ["FlexibleRetire Savings Scheme", "Flexibility to change contribution", "₹10,000 per month", "Age 22-58 years", "flexibleretire@example.com", "1800-234-5670"],
    ["SavingsPlus Retirement Annuity", "Additional savings options", "₹60,000 annually", "Age 30-65 years", "savingsplus@example.com", "1800-456-7890"],
    ["FutureDream Pension Fund", "Growth-oriented investment", "₹14,000 monthly SIP", "Age 20-50 years", "futuredream@example.com", "1800-890-1234"],
    ["PioneerRetire Plan", "Early retirement option", "₹35,000 per annum", "Age 25-55 years", "pioneerretire@example.com", "1800-567-8901"],
    ["SmartSecure Retirement Scheme", "Secure investment with insurance", "₹22,000 quarterly", "Age 30-65 years", "smartsecure@example.com", "1800-234-5678"],
    ["GoldenOpportunity Pension", "Opportunity for high returns", "₹1,80,000 lump sum", "Age 28-60 years", "goldenopportunity@example.com", "1800-876-5432"],
    ["SunsetRetire Annuity", "Guaranteed principal protection", "₹18,000 per annum", "Age 35-70 years", "sunsetretire@example.com", "1800-345-6789"],
    ["EasyLife Pension Plan", "Simplified investment process", "₹8,000 per month", "Age 22-58 years", "easylife@example.com", "1800-789-0123"],
    ["SteadyGrowth Retirement Fund", "Steady and consistent growth", "₹12,000 monthly SIP", "Age 25-55 years", "steadygrowth@example.com", "1800-234-5670"],
    ["SecureFuture Savings Scheme", "Insurance coverage with savings", "₹50,000 annually", "Age 30-65 years", "securefuture@example.com", "1800-456-7890"],
    ["DreamBuilder Pension Fund", "Build your dream retirement", "₹16,000 monthly SIP", "Age 20-50 years", "dreambuilder@example.com", "1800-890-1234"],
]

columns = ["Plan Name", "Features", "Minimum Investment", "Eligibility", "Contact Email", "Contact Number"]
df = pd.DataFrame(data, columns=columns)
df.to_csv('retirement_plans.csv', index=False)