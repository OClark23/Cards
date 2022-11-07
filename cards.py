class Card {
   public static final int SPADE   = 4;
   public static final int HEART   = 3;
   public static final int CLUB    = 2;
   public static final int DIAMOND = 1;

   private int rank;
   private int suit;
   private static final String[] Suit = {"Hearts", "Clubs", "Spades", "Diamonds"};
   private static final String[] Rank = {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"};                     

   private int cardSuit;
   private int cardRank;

   public Card(int suit, int rank) {
      if (rank == 1)
         cardRank = 14;     // Give Ace the rank 14
      else
         cardRank = (int) rank;
         cardSuit = (int) suit;
   }

   public int suit() {
      return this.cardSuit;         
   }

   public String suitStr() {
      return(this.Suit[ this.cardSuit ]);                                
   }

   public int rank() {
      return this.cardRank;
   }

   public String rankStr() {
      return ( Rank[ cardRank ] );
   }


   public String toString() {
      return ( Rank[ cardRank ] + Suit[ cardSuit ] );
   }
}
