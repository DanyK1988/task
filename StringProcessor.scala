object StringProcessor {
//Проверяем длинну слова, если больше 3, то возвращаем True, в противном случае False
  def check_length(str: String): Boolean = {
    if (str.length > 3) {
      true
    } else {
      false
    }
  }

// Переводим слово в верхний регистр
  def upper_case(str: String): String = {
    str.toUpperCase()
  }

  def processStrings(strings: List[String]): List[String] = {
    val result = strings.filter(check_length).map(upper_case)
    result
    }

  def main(args: Array[String]): Unit = {
    val strings = List("apple", "cat", "banana", "dog", "elephant")
    val processedStrings = processStrings(strings)
    println(s"Processed strings: $processedStrings")
    }
}