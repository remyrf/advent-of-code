import Foundation

func isValid(_ passphrase: Substring) -> Bool {
    let words = passphrase.split(separator: " ")

    for (i, word) in words.enumerated() {
        for (j, otherWord) in words.enumerated() {
            if i == j {
                continue
            }

            if word == otherWord || word.sorted() == otherWord.sorted() {
                return false
            }
        }
    }

    return true
}

let url = URL(filePath: "input.txt")
let contents = try! String(contentsOf: url, encoding: String.Encoding.utf8)

let lines = contents.split(separator: "\n")
var total = lines.count(where: isValid)

print(total)
