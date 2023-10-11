def main():
    exam_st_date = "11: 12: 2014"
    parts = exam_st_date.split(": ")
    day = parts[0]
    month = parts[1]
    year = parts[2]

    formatted_date = "{}/{}/{}".format(day, month, year)
    print("The examination will start from:", formatted_date)


if __name__ == "__main__":
    main()
