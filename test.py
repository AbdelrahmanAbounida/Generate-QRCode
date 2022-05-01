import nlpcloud

client = nlpcloud.Client("roberta-base-squad2", "ad2ac4879d59af6bb4a3aff9302f99367b6ff75d",gpu=False)
print(client.question
      ("As 2022 begins, and you're joining us from France, there’s a new year resolution we’d like you to consider."
       " Tens of millions have placed their trust in the Guardian’s fearless journalism since we started publishing 200 years ago,"
       " turning to us in moments of crisis, uncertainty, solidarity and hope. We’d like to invite you to join more than 1.5 million supporters,"
       " from 180 countries, who now power us financially – keeping us open to all, and fiercely independent. Unlike many others, the Guardian"
       " has no shareholders and no billionaire owner. Just the determination and passion to deliver high-impact global reporting, always "
       "free from commercial or political influence. Reporting like this is vital for democracy, for fairness and to demand better from the powerful.",
    "When was the Guardian created?"))