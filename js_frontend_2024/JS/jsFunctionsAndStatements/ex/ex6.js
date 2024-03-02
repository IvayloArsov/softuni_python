function validatePassword(password) {
  const errors = [];

  if (password.length < 6 || password.length > 10) {
    errors.push("Password must be between 6 and 10 characters");
  }

  if (!/^[a-zA-Z0-9]+$/.test(password)) {
    errors.push("Password must consist only of letters and digits");
  }

  const digitCount = password
    .split("")
    .filter((char) => /\d/.test(char)).length;
  if (digitCount < 2) {
    errors.push("Password must have at least 2 digits");
  }

  return errors.length === 0 ? "Password is valid" : errors.join("\n");
}

validatePassword("Pa$s$s");
