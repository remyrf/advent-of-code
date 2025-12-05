import Foundation

struct Spot {
    var number = 0
    var found = false
}

let input = try! String(contentsOf: URL(filePath: "input.txt"), encoding: String.Encoding.utf8)
let segments = input.split(separator: "\n\n")
let sequence = segments[0].split(separator: ",").map({ Int($0) ?? 0 })
let boardsStrs = segments[1...]
var boards = boardsStrs.map({
    $0.split(separator: "\n").map({
        $0.split(separator: " ").map({ Spot(number: Int($0) ?? 0) })
    })
})

var winner: [[Spot]]? = nil
var winningNum = 0
var winningIndexes: [Int] = []
outer: for (x, num) in sequence.enumerated() {
    for (i, board) in boards.enumerated() {
        for (j, row) in board.enumerated() {
            for (k, spot) in row.enumerated() {
                if spot.number == num {
                    boards[i][j][k].found = true
                }
            }
        }

        for row in 0..<board.count {
            if !winningIndexes.contains(i) && board[row].allSatisfy({ $0.found }) {
                winner = board
                winningNum = sequence[x - 1]
                winningIndexes.append(i)
            }
        }

        for col in 0..<board[0].count {
            var allFound = true
            for row in 0..<board.count {
                if !board[row][col].found {
                    allFound = false
                    break
                }
            }
            if allFound && !winningIndexes.contains(i) {
                winner = board
                winningNum = sequence[x - 1]
                winningIndexes.append(i)
            }
        }
    }
}

if let win = winner {
    var sum = 0
    for row in win {
        for spot in row {
            if !spot.found {
                sum += spot.number
            }
        }
    }
    print(sum * winningNum)
}
