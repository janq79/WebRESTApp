if (TEST_MODE == '2' && (BACKEND_FUNCTION == 'add' || BACKEND_FUNCTION == 'update')) {
    return "<input type='text' name='value' value='defaultUser'/>"
} else {
    return ""
}