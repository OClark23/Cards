public int rank() {
      return this.cardRank;         
   }

   public String toString() {
      return Rank[rank-1] + " of " + Suit[suit-1];
   }

   public boolean equals(Card other) {
      if (other == null)  // Check for null argument.
         throw new NullPointerException("Argument is null.");

      if ((this.suit == other.suit()) && (this.rank == other.rank()))  // Check suit and rank equality.
         return true;                                                   // Return true if they are equal, false otherwise.

      else  // If the above conditions are not met, then the cards are not equal, so return false here as well!
         return false;      				                 	   	    	        }

    @Override                           // Override the Object class's equals method! This is important because we need to override it in order to use Card objects as keys in HashMap objects! We will be using these hash maps as a way of storing our card decks in memory so that we can quickly check whether or not a certain card exists within them without having to iterate through all 52 cards and compare each one individually! We will also be using these hash maps when checking whether or not a player has won by comparing their hand against the dealer's hand since we need to know which cards were dealt out before any players have had their hands checked against each other...and those two sets of hands should never contain any duplicate cards at all!! So let's make sure that this method overrides Object's equals method properly so that we can use Card objects as keys in HashMaps!! :D :D :D ! ^_^ ! ^_^ ! ^_^ ! ^_^ ! ^_^ ! ^_^ ! ^_^ ! ^_^ !!!!! :) :) :) :) :) :) )))))))) D: D: D: D: D: D: D: D:");             /* The following code was taken from https://www.geeksforgeeks.org/overriding-equals-method-in-java/ */

    @Override                         /* Override the Object class's equals method! This is important because we need to override it in order to use Card objects as keys in HashMap objects! We will be using these hash maps as a way of storing our card decks
