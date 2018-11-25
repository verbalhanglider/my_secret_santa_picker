
from random import randint, sample
from unittest import TestCase

class TestSecretSanta(TestCase):
    def setUp(self):
        self.participant_options = \
                ['a','b','c','d','e','f','g','h','i','j','k',
                 'l','m','n','o','p','q','r','s','t','u','v',
                 'w','x','y','z']

    def teardown(self):
        pass

    def _get_participants(participants):
        from secretsanta import assign
        results = assign(participants)
        
    def test_regression_test_noone_give_to_self(self):
        from secretsanta import assign
        for x in range(0,100):
            number_participants = randint(1,20)
            participants = sample(self.participant_options, 
                                  number_participants)
            assignments = assign(participants)
            for k,v in assignments.items():
                self.assertNotEqual(k,v)

    def test_regression_test_same_number_givers_as_receivers(self):
        from secretsanta import assign
        for x in range(2,100):
            number_participants = randint(2,20)
            participants = sample(self.participant_options,
                                  number_participants)
            total = len(participants)
            assignments = assign(participants)
            givers = [x for x in assignments.keys()]
            receivers = [assignments[x] for x in assignments.keys()]
            self.assertEqual(set(givers), set(receivers))

    def test_regression_test_same_numher_gives_receivers_and_participants(self):
        from secretsanta import assign
        for x in range(0,100):
            number_participants = randint(2,20)
            participants = sample(self.participant_options,
                                  number_participants)
            total = len(participants)
            assignments = assign(participants)
            givers = [x for x in assignments.keys()]
            receivers = [assignments[x] for x in assignments.keys()]
            checks = [len(lst) == total for lst in 
                    [givers, receivers, participants]]
            self.assertTrue(all(checks)) 
