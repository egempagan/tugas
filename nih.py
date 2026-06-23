import requests

def tampilkan_identitas():

    print("\nIDENTITAS PESERTA UJIAN")

    print("Nama : Muhammad Reivan")

    print("NIM  : 8020250116")

def ambil_data_api():

    url = "https://dummyjson.com/quotes"

    try:

        response = requests.get(url, timeout=10)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:

        print("\nTerjadi kesalahan saat mengambil data API.")

        print("Detail Error :", error)

        return None

def tampilkan_quotes(data):

    print("\nDAFTAR KUTIPAN (QUOTES)")

    print()

    jumlah_data = len(data["quotes"])

    for nomor, quote in enumerate(data["quotes"], start=1):

        print(f"Data Ke-{nomor}")

        print(f"ID     : {quote['id']}")

        print(f"Quote  : {quote['quote']}")

        print(f"Author : {quote['author']}")

        print()

    print(f"Total Data Quote : {jumlah_data}")

def main():

    tampilkan_identitas()

    data = ambil_data_api()

    if data:

        tampilkan_quotes(data)

if __name__ == "__main__":

    main()
