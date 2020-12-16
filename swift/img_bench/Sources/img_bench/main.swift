import SwiftImage
import Benchmark
import PNG

let image = Image<RGBA<UInt8>>(contentsOfFile: "icon01.png")!
// let (pixels, (x: width, y: height)) = try PNG.rgba(path: "example.png", of: UInt8.self)

let (pixels, (x: width, y: height)) = try PNG.rgba(path: "icon01.png", of: UInt8.self)

benchmark("SwiftImage") {
    for _ in 1 ... 100 {
        let image = Image<RGBA<UInt8>>(contentsOfFile: "icon01.png")
    }
}

benchmark("Pnglib") {
    for _ in 1 ... 100 {
        let (pixels, (x: width, y: height)) = try PNG.rgba(path: "icon01.png", of: UInt8.self)
    }
}

Benchmark.main()

print(image.height)
print(height)
print("Hello, world!")
