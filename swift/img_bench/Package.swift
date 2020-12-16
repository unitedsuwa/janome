// swift-tools-version:5.3
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "img_bench",
    dependencies: [
        // Dependencies declare other packages that this package depends on.
        // .package(url: /* package url */, from: "1.0.0"),
            .package(name: "SwiftImage", url: "https://github.com/koher/swift-image", from: "0.7.1"),
            // .package(url: "https://github.com/koher/swift-image", from: "0.7.1"),
            .package(name: "PNG", url: "https://github.com/kelvin13/png", from: "3.0.2"),
            .package(name: "Benchmark", url: "https://github.com/google/swift-benchmark", from: "0.1.0"),

    ],
    targets: [
        // Targets are the basic building blocks of a package. A target can define a module or a test suite.
        // Targets can depend on other targets in this package, and on products in packages this package depends on.
        .target(
            name: "img_bench",
            dependencies: [
                "SwiftImage",
                "PNG",
                "Benchmark"
             ]
        ),

        .testTarget(
            name: "img_benchTests",
            dependencies: ["img_bench"]),
    ]
)
