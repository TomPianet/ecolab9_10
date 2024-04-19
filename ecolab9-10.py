from IPython.display import HTML

# Use the direct URL to the GIF
HTML('<img src="https://media1.tenor.com/m/xrUe4KFY0dsAAAAC/brother-ew-ew.gif" width="800">')


dates = pd.date_range("20230309", periods=6, freq="MS")

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
# df = pd.DataFrame(np.random.randint(1, 100, (6, 4)), index=dates, columns=list("ABCD"))

df

# df.T.index


df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo"
    }
)
df2



print(df.index)
print("-----")
df.describe()


print(df.T)

print(df.sort_values(by="B", ascending=False))
print(df)

print(df)
print(df["A"]) # df.A dot notation
print("----")
print(type(df.A))
print(df.A.values)


# slice
df[1:3]["A"]


# selection withb loc (by value)

dates[1] # this is the index for the second row
print(df)
print("-----")
print(df.loc[dates[1]])


print(df)
print("----")
print(df.iloc[1])
print("----")
print(df.iloc[1:3, 1:2])
print("----")
print(df.iloc[[0,2,4], [1,3]])


df["E"] = ["car", "toy"] * 2 + ["ship"]
df["James"] = [7] * 5
df["James"] = 11
print(df)
