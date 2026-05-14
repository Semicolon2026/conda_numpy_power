from app.utils import load_csv, clean_columns

def run():
    df = load_csv("data/sample.csv")
    df = clean_columns(df)

    print("[INFO] Preprocessing complete")
    print(df.head())

if __name__ == "__main__":
    run()
