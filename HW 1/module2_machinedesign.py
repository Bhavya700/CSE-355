from cse355_machine_design import DFA, registry


def problem1():
    """
    L_1 = {w in {0,1}* | w contains 010 as a substring}
    """

    Q = {"q_0","q0","q01","q010"}
    Sigma = {"0","1"}
    delta = {
        ("q_0","0"):"q0",
        ("q_0","1"):"q_0",
        ("q0","0"):"q0",
        ("q0","1"):"q01",
        ("q01","0"):"q010",
        ("q01","1"):"q_0",
        ("q010","0"):"q010",
        ("q010","1"):"q010"
    }
    q0 = "q_0"
    F = {"q010"}

    return DFA(Q, Sigma, delta, q0, F)


def problem2():
    """
    L_2 = {w in {0,1}* | w does not contain 100 as a substring}
    """

    Q = {"q_0","q1","q10","q100"}
    Sigma = {"0","1"}
    delta = {
        ("q_0","0"):"q_0",
        ("q_0","1"):"q1",
        ("q1","0"):"q10",
        ("q1","1"):"q1",
        ("q10","0"):"q100",
        ("q10","1"):"q1",
        ("q100","0"):"q100",
        ("q100","1"):"q100"
    }
    q0 = "q_0"
    F = {"q_0","q1","q10"}

    return DFA(Q, Sigma, delta, q0, F)

def problem3():
    """
    L_3 = {w in {a,b}* | |w| < 4}
    """

    Q = {"q0","q1","q2","q3","qov"}
    Sigma = {"a","b"}
    delta = {
        ("q0","a"):"q1",
        ("q0","b"):"q1",
        ("q1","a"):"q2",
        ("q1","b"):"q2",
        ("q2","a"):"q3",
        ("q2","b"):"q3",
        ("q3","a"):"qov",
        ("q3","b"):"qov",
        ("qov","a"):"qov",
        ("qov","b"):"qov"
    }
    q0 = "q0"
    F = {"q3","q2","q1","q0"}

    return DFA(Q, Sigma, delta, q0, F)


def problem4():
    """
    L_4 = {w in {a,b,c}* | w has an even number of b's}
    """

    Q = {"q_0","q1","q2"}
    Sigma = {"a","b","c"}
    delta = {
        ("q_0","a"):"q2",
        ("q_0","b"):"q1",
        ("q_0","c"):"q2",
        ("q1","a"):"q1",
        ("q1","b"):"q2",
        ("q1","c"):"q1",
        ("q2","a"):"q2",
        ("q2","b"):"q1",
        ("q2","c"):"q2"
    }
    q0 = "q_0"
    F = {"q2","q_0"}

    return DFA(Q, Sigma, delta, q0, F)


def problem5():
    """
    L_5 = {epsilon, 0, 101} on Sigma = {0, 1}
    """

    Q = {"qe","q0","q1","q10","q101","qn"}
    Sigma = {"0","1"}
    delta = {
        ("qe","0"):"q0",
        ("qe","1"):"q1",
        ("q0","0"):"qn",
        ("q0","1"):"qn",
        ("q1","0"):"q10",
        ("q1","1"):"qn",
        ("q10","0"):"qn",
        ("q10","1"):"q101",
        ("q101","0"):"qn",
        ("q101","1"):"qn",
        ("qn","0"):"qn",
        ("qn","1"):"qn",
    }
    q0 = "qe"
    F = {"qe","q0","q101"}

    return DFA(Q, Sigma, delta, q0, F)


def problem6():
    """L_6 = {w in {1}* | |w| is a multiple of 2 or 3}"""

    Q = {"qb","q1","q2","q3","q4","q5"}
    Sigma = {"1"}
    delta = {
        ("qb","1"):"q1",
        ("q1","1"):"q2",
        ("q2","1"):"q3",
        ("q3","1"):"q4",
        ("q4","1"):"q5",
        ("q5","1"):"qb",
    }
    q0 = "qb"
    F = {"q2","q3","qb","q4"}
    return DFA(Q, Sigma, delta, q0, F)


def problem7():
    """L_7 = {w in {a,b}* | w has an even number of a's, contains aab as a substring, or both}"""

    Q = {"q_0","q00","q01","q02","q03","q10","q11","q12","q13"}
    Sigma = {"a","b"}
    delta = {
        ("q_0","a"):"q11",
        ("q_0","b"):"q00",
        ("q00","a"):"q11",
        ("q00","b"):"q00",
        ("q01","a"):"q12",
        ("q01","b"):"q00",
        ("q02","a"):"q12",
        ("q02","b"):"q03",
        ("q03","a"):"q13",
        ("q03","b"):"q03",
        ("q10","a"):"q01",
        ("q10","b"):"q10",
        ("q11","a"):"q02",
        ("q11","b"):"q10",
        ("q12","a"):"q02",
        ("q12","b"):"q13",
        ("q13","a"):"q03",
        ("q13","b"):"q13"
    }
    q0 = "q_0"
    F = {"q_0","q00","q01","q02","q03","q13"}
    return DFA(Q, Sigma, delta, q0, F)


if __name__ == "__main__":
    problem1().submit_as_answer(1)
    problem2().submit_as_answer(2)
    problem3().submit_as_answer(3)
    problem4().submit_as_answer(4)
    problem5().submit_as_answer(5)
    problem6().submit_as_answer(6)
    problem7().submit_as_answer(7)
    registry.export_submissions()
