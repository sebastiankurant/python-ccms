from model.employee import Employee


class Mentor(Employee):
    """
    Represents Mentor object.
    """

    @classmethod
    def get_by_id(cls, id):
        """
        Get mentor by id from database.
        arguments: int(mentor id)
        return: obj(Mentor)
        """
        return super(Mentor, cls).get_by_id(id, 'mentor')

    @classmethod
    def list_mentors(cls):
        """
        Returns list of mentors object from database.
        return: list(list of Mentor objects)
        """
        return super(Mentor, cls).list_employee('mentor')
