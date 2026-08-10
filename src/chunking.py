text = "Toys for Bob, Inc. is an American video game developer based in Novato, California, and founded in 1989. The founders, Paul Reiche III and Fred Ford (both pictured), met when Reiche sought a programmer to develop Star Control, and developed several games, including The Horde, Pandemonium!, and The Unholy War. In the early 2000s, the studio transitioned to working on licensed games before being laid off by Crystal Dynamics. It was incorporated in 2002 and Activision became their publisher before they acquired the studio in 2005. Credited with inventing the toys-to-life genre, the 2011 release of Skylanders: Spyro's Adventure was considered a technological and commercial breakthrough. In 2018, Toys for Bob assisted with the remaster compilations Crash Bandicoot N. Sane Trilogy and Spyro Reignited Trilogy. The founders left the company in 2020. Microsoft acquired the holding in October 2023 and the studio spun off from Activision in May 2024."


def create_chunks(text,chunk_size=100, overlap=20):

    chunks = []
    start = 0

    while(start < len(text)):
        end = start + chunk_size

        chunk = text[start : end]
        chunks.append(chunk)

        start += chunk_size-overlap

    return chunks 

chunks = create_chunks(text)

print("number of chunks : ",len(chunks))
print(chunks[0])