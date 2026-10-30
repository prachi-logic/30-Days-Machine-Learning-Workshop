#DATASET----
# import pandas as pd

# data = {
#     "name": ["a", "b", "c", "d", "e"],
#     "roll_no": [1, 2, 3, 4, 5],
#     "marks": [35, 46, 88, 75, 19],  # Added a 5th mark
# }

# df = pd.DataFrame(data)  # Fixed 'DataFrame' capitalization
# print(df)
# print(df["name"])

# #----ADD NEW COLUMN-----
# df["stay"]=["h","d","h","d", "d"]
# print(df)


# df.shape
# df.columns 
# df.info()


# #loc and iloc-----
# #way of selcting values using their indexes....
# # df.loc[0]
# # df.set_index("name",inplace=True)
# # print(df )

# # df.iloc["a"]


# print(df[df["marks"] >35])
# print(df[df["marks"] >35]) ([df["stay"]=="d")])



# import pandas as pd

# data = {
#     "name": ["a", "b", "c", "d", "e"],
#     "roll_no": [1, 2, 3, 4, 5],
#     "marks": [35, 46, 88, 75, 19],
# }

# df = pd.DataFrame(data)

# # Add new column
# df["stay"] = ["h", "d", "h", "d", "d"]

# # Correct syntax for multiple conditions (AND logic using &):
# filtered_df = df[(df["marks"] > 35) & (df["stay"] == "d")]
# print(filtered_df)




import pandas as pd

# Create dataset
data = {
    "name": ["a", "b", "c", "d", "e"],
    "roll_no": [1, 2, 3, 4, 5],
    "marks": [35, 46, 88, 75, 19]
}

df = pd.DataFrame(data)

# Add new column
df["stay"] = ["h", "d", "h", "d", "d"]

# Basic information
print("Complete Dataset:")
print(df)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nInformation:")
df.info()

# Select using loc
print("\nFirst Row:")
print(df.loc[0])

# Select using iloc
print("\nFirst Row using iloc:")
print(df.iloc[0])

# Filter marks greater than 35
print("\nMarks greater than 35:")
print(df[df["marks"] > 35])

# Multiple conditions (AND)
print("\nMarks > 35 AND stay == d:")
filtered_df = df[(df["marks"] > 35) & (df["stay"] == "d")]

print(filtered_df)
