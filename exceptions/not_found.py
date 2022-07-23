class NotFoundError(Exception):

    entity_name: str

    def __init__(self, entity_id):
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")


class ArtistNotFoundError(NotFoundError):

    entity_name = "Artist"


class AlbumNotFoundError(NotFoundError):

    entity_name = "Album"


class TrackNotFoundError(NotFoundError):

    entity_name = "Track"
