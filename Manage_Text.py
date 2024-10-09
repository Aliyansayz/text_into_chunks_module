class Manage_Text:
    def __init__(self, text, chunk_size=1000, chunk_overlap=100):
        """
        Initialize with text and chunking parameters.

        Args:
            text (str): The large text to be split into chunks.
            chunk_size (int): The maximum size of each chunk in characters.
            chunk_overlap (int): The number of characters to overlap between consecutive chunks.
        """
        self.text = text
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def splitting_with_chunks(self):
        """
        Split the text into chunks using list slicing.

        Returns:
            List of text chunks with the specified chunk size and overlap.
        """
        # Initialize an empty list to store the chunks
        chunks = []

        # Iterate over the text using a step size of (chunk_size - chunk_overlap)
        step = self.chunk_size - self.chunk_overlap # step size will be remainder of overlap text size we want in this way we are lagging
        # by similar chunk size, the size we want to overlap


        # Generate chunks using list slicing
        for i in range(0, len(self.text), step):
            chunk = self.text[i:i + self.chunk_size]
            chunks.append(chunk)

        return chunks


