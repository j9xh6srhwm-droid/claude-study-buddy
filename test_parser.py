from mode_parser import parse_mode

def test(description, input_str, expected_mode, expected_content_fragment):
    mode, _, content = parse_mode(input_str)
    mode_ok    = mode == expected_mode
    content_ok = expected_content_fragment.lower() in content.lower()
    status = "PASS" if (mode_ok and content_ok) else "FAIL"
    print(f"  [{status}] {description}")
    if status == "FAIL":
        print(f"         mode: got '{mode}', expected '{expected_mode}'")
        print(f"         content: got '{content}', expected fragment '{expected_content_fragment}'")

print("\nRunning parser tests...\n")
test("explain prefix",         "/explain tokens",       "explain", "tokens")
test("quiz prefix",            "/quiz context window",  "quiz",    "context window")
test("summary prefix",         "/summary",              "summary", "")
test("no prefix → default",    "what is a token?",      "explain", "what is a token")
test("unknown prefix → default", "/unknown topic",      "explain", "unknown topic")
test("uppercase prefix",       "/QUIZ embeddings",      "quiz",    "embeddings")
print()