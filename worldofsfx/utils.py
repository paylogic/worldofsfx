import arrow


def utc_now():
    """Date utility that returns a :obj:`datetime.datetime` objects set to
    utc. Useful for setting default datetimes on SqlAlchemy model fields.

    This utility currently depends on the fanatsic arrow library.
    .. _a link: https://github.com/crsmithdev/arrow

    Useage::

        from worldofsfx.database import db
        from worldofsfx.utils import utc_now

        class Model(db.Model):

            created = db.Column(db.DateTime, default=utc_now)

    :returns: utc datetime object
    :rtype: :obj:`datetime.datetime`
    """

    return arrow.utcnow().datetime
