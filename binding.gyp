{
  "targets": [
    {
      "target_name": "steamworks",
      "sources": [
        "steam_api_wrap.cxx"
      ],
      "include_dirs": [
        ".",
        ".\\sdk\\public\\steam"
      ],
      "libraries": [
        "..\\steam_api64.lib",
        "..\\sdkencryptedappticket64.lib"
      ]
    }
  ]
}