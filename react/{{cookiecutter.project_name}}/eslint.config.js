import stylistic from "@stylistic/eslint-plugin";
import globals from "globals";
import eslint from "@eslint/js";
import tsParser from "@typescript-eslint/parser";
import reactRefresh from "eslint-plugin-react-refresh";
import tseslint from "typescript-eslint";

export default tseslint.config(
  eslint.configs.recommended,
  tseslint.configs.recommendedTypeChecked,
  tseslint.configs.stylistic,
  stylistic.configs["all-flat"],
  {
    "ignores": [
      "node_modules",
      "build",
      "dist",
    ],
    "files": ["**/*.{js,jsx,mjs,cjs,ts,tsx}"],
    "languageOptions": {
      "sourceType": "module",
      "globals": {
        ...globals.browser,
        ...globals.node,
      },
      "parser": tsParser,
      "parserOptions": {
        "projectService": true,
        "tsconfigRootDir": import.meta.dirname,
        "sourceType": "module",
        "ecmaFeatures": {
          "jsx": true,
        },
      },
    },
    "plugins": {
      "@stylistic": stylistic,
      "react-refresh": reactRefresh,
    },
    "rules": {
      "react-refresh/only-export-components": "error",
      "semi": "error",
      "quotes": [
        "error",
        "double",
      ],
      "@stylistic/indent": [
        "error",
        2,
      ],
      "@stylistic/comma-dangle": [
        "error",
        "always-multiline",
      ],
    },
  },
  {
    "files": [
      "eslint.config.js",
      "tailwind.config.js",
      "postcss.config.js",
      "vite.config.ts",
    ],
    "extends": [tseslint.configs.disableTypeChecked],
  },
);
