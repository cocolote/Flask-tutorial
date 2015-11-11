import os
import flaskr
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/')

# expect to display "No entries so far" when the database is empty
    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'No entries here so far' in str(rv.data)

# login helper
    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password,
        ), follow_redirects=True)

# logout helper
    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

# test login and logout also login with invalid credentials
    def test_login_logout(self):
        rv = self.login('admin', 'default')
        assert 'You were logged in' in str(rv.data)
        rv = self.logout()
        assert 'You were logged out' in str(rv.data)
        rv = self.login('Ezequiel', 'default')
        assert 'Invalid username' in str(rv.data)
        rv = self.login('admin', '1234')
        assert 'Invalid password' in str(rv.data)

# test adding messages
    def test_messages(self):
        self.login('admin', 'default')
        rv = self.app.post('/add', data=dict(
            title='<Hello>',
            text='<strong>HTML</strong> allowed here',
        ), follow_redirects=True)
        assert 'No entries here so far' not in str(rv.data)
        assert '&lt;Hello&gt;' in str(rv.data)
        assert '<strong>HTML</strong> allowed here' in str(rv.data)

if __name__ == '__main__':
    unittest.main()
