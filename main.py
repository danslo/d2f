"""
query {
  game(name: "Dota 2") {
    streams(first: 30, after: null) {
      edges {
        cursor
        node {
          viewersCount
          broadcaster {
            displayName
          }
        }
      }
    }
  }
}
"""

def main():
    print("Hello World!")


if __name__ == "__main__":
    main()