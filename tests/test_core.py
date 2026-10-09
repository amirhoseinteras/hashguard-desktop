import tempfile,unittest,hashlib
from pathlib import Path
from hashguard import sha256_file,verify_digest
class Tests(unittest.TestCase):
    def test_integrity(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"file";p.write_bytes(b"hello")
            digest=hashlib.sha256(b"hello").hexdigest()
            self.assertEqual(sha256_file(p),digest)
            self.assertTrue(verify_digest(digest,digest))
            self.assertFalse(verify_digest(digest,"0"*64))
    def test_invalid(self):
        with self.assertRaises(ValueError):verify_digest("0"*64,"nothex")
